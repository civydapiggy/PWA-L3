from django import template
from cart.models import Cart

register = template.Library()

@register.filter
def cart_total_quantity(user):
    if getattr(user, "is_authenticated", False):
        return Cart.get_cart_quantity(user)
    return 0

# NEW: multiply helper for totals
@register.filter
def multiply(a, b):
    try:
        return float(a) * float(b)
    except (TypeError, ValueError):
        return 0

# Optional: total $ for current user's cart
@register.filter
def cart_total_sum(user):
    if not getattr(user, "is_authenticated", False):
        return 0
    qs = Cart.objects.filter(user=user)
    return sum((c.quantity or 0) * float(getattr(c.item, "price", 0)) for c in qs)