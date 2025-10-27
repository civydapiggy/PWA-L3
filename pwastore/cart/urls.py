from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_home, name='cart-home'),
    path('add/<slug:slug>/', views.add_to_cart, name='add-to-cart'),  # <-- changed here
    path('increase/<slug:slug>/', views.increase_cart, name='increase-cart'),
    path('decrease/<slug:slug>/', views.decrease_cart, name='decrease-cart'),
    path('remove/<slug:slug>/', views.remove_cart, name='remove-cart'),
    path('clear/', views.clear_cart, name='clear-cart'),
]