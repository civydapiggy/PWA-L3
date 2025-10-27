from django.urls import path
from . import views

# ✅ import the orders views directly
from orders.views import OrderCreateView, OrderCompleteView

app_name = "store_products"

urlpatterns = [
    path("", views.product_list, name="home"),
    path("product/<int:pk>/", views.product_detail, name="product-detail"),
    path("products/<slug:category_slug>/", views.products_by_category, name="products-by-category"),
    path("cart/add/<slug:slug>/", views.add_product_to_cart, name="add-to-cart"),

    # ✅ PROXY ORDERS ROUTES so /orders/... works even without orders include
    path("orders/create/", OrderCreateView.as_view(), name="order-create-proxy"),
    path("orders/complete/<int:pk>/", OrderCompleteView.as_view(), name="order-complete-proxy"),
]