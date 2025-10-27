from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.utils.text import slugify
from .models import Product, Category

# import the cart handler and alias it to avoid name clashes
from cart.views import add_to_cart as cart_add_to_cart


def _nav_categories():
    """Return categories for navbar: primary ones if set, otherwise all."""
    cats = Category.objects.filter(primaryCategory=True).order_by('title')
    if not cats.exists():
        cats = Category.objects.all().order_by('title')
    return cats


# HOME — only featured products
def product_list(request):
    products = Product.objects.filter(featured=True)
    return render(request, 'store_products/home.html', {
        'all_products_list': products,
        'categories': _nav_categories(),
    })


# PRODUCT DETAIL
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store_products/product_detail.html', {
        'product': product,
        'categories': _nav_categories(),
    })


# CATEGORY LISTING (slug-safe)
def products_by_category(request, category_slug):
    """
    Resolve the category by comparing slugify(category.title) to the URL slug.
    Works for titles like 'T-Shirts', 'T Shirts', etc.
    """
    category = None
    for c in Category.objects.all():
        if slugify(c.title) == category_slug:
            category = c
            break
    if category is None:
        raise Http404("Category not found")

    products = Product.objects.filter(category=category)
    return render(request, 'store_products/products_by_category.html', {
        'category': category,
        'all_products_list': products,
        'categories': _nav_categories(),
    })


# ADD TO CART (wrapper that forwards to cart app)
# Assumes your cart.add_to_cart expects a product SLUG.
def add_product_to_cart(request, slug):
    return cart_add_to_cart(request, slug)