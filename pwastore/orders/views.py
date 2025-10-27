from datetime import timedelta
from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib import messages

from .models import Order, OrderItem
# Adjust this import to match your real app label. If your app is literally "cart",
# this should be: from cart.models import Cart
from cart.models import Cart


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'city', 'province', 'postalcode']


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_qs = Cart.objects.filter(user=self.request.user)
        context['cart_list'] = cart_qs
        # simple total for display
        context['cart_total'] = sum((c.quantity or 0) * float(c.item.price) for c in cart_qs)
        return context

    def post(self, request, *args, **kwargs):
        cart_qs = Cart.objects.filter(user=request.user)
        # prevent empty cart orders
        has_items = any((c.quantity or 0) > 0 for c in cart_qs)
        if not has_items:
            messages.error(request, "Your cart is empty. Please add items before placing an order.")
            form = self.form_class(request.POST or None)
            return render(request, 'orders/order_create.html', {
                'form': form,
                'cart_list': cart_qs,
                'cart_total': 0.0,
            })

        form = self.form_class(request.POST)
        if form.is_valid():
            # create the order
            form.instance.user = request.user
            form.instance.orderdate = timezone.now()
            form.instance.shippingdate = form.instance.orderdate + timedelta(days=3)
            order = form.save()

            # move cart items into OrderItem
            for cart_item in cart_qs:
                qty = int(cart_item.quantity or 0)
                if qty > 0:
                    oi, _ = OrderItem.objects.get_or_create(
                        order=order,
                        item=cart_item.item,
                        defaults={'quantity': 0, 'price': 0},
                    )
                    oi.quantity = qty
                    oi.price = float(cart_item.item.price)
                    oi.save()
                cart_item.delete()  # clear cart regardless

            return redirect(f'/orders/complete/{order.pk}/')

        # invalid form
        return render(request, 'orders/order_create.html', {
            'form': form,
            'cart_list': cart_qs,
            'cart_total': sum((c.quantity or 0) * float(c.item.price) for c in cart_qs),
        })


class OrderCompleteView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_complete.html'
    context_object_name = 'order'

    # (optional) ensure users can only see their own orders
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)