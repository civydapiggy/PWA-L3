from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cart
from store_products.models import Product

# Helper: get or create cart item & increase quantity
def _increase_cart(user, slug):
    item = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(item=item, user=user)
    if created:
        cart.quantity = 1
    else:
        cart.quantity += 1
    cart.save()
    return cart

# Add to cart (from product page)
@login_required
def add_to_cart(request, slug):
    cart = _increase_cart(request.user, slug)
    if cart.quantity == 1:
        messages.info(request, f"{cart.item.name} has been added to your cart.")
    else:
        messages.info(request, f"{cart.item.name} quantity updated to {cart.quantity}.")
    return redirect('store_products:home')

# Increase quantity (from cart page + button)
@login_required
def increase_cart(request, slug):
    cart = _increase_cart(request.user, slug)
    messages.info(request, f"{cart.item.name} quantity increased to {cart.quantity}.")
    return redirect('cart:cart-home')

# Decrease quantity (from cart page - button)
@login_required
def decrease_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
            messages.info(request, f"{cart.item.name} quantity decreased to {cart.quantity}.")
        else:
            cart.delete()
            messages.info(request, f"{cart.item.name} removed from your cart.")
    return redirect('cart:cart-home')

# Remove item entirely
@login_required
def remove_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart_qs.delete()
        messages.info(request, f"{item.name} removed from your cart.")
    return redirect('cart:cart-home')

# Cart home page
@login_required
def cart_home(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_quantity = Cart.get_cart_quantity(request.user)
    total_sum = Cart.get_cart_sum(request.user)
    return render(request, "cart/home.html", {
        "cart_items": cart_items,
        "total_quantity": total_quantity,
        "total_sum": total_sum,
    })

@login_required
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    messages.info(request, "Your cart has been cleared.")
    return redirect('cart:cart-home')