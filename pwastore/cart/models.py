from django.db import models
from django.contrib.auth import get_user_model
from store_products.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='in_carts')
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')  # ensures one entry per product per user

    def __str__(self):
        return f"{self.user.username} - {self.item.name} ({self.quantity})"

    def get_total(self):
        return self.item.price * self.quantity

    @classmethod
    def get_cart_quantity(cls, user):
        if user.is_authenticated:
            return sum(cart.quantity for cart in cls.objects.filter(user=user))
        return 0

    @classmethod
    def get_cart_sum(cls, user):
        if user.is_authenticated:
            return sum(cart.get_total() for cart in cls.objects.filter(user=user))
        return 0