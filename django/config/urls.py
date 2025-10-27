# pwastore/config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views as page_views

urlpatterns = [
    # Home page
    path('', page_views.home, name='home'),

    # Store products (mounted at root: '', so existing product URLs keep working)
    path('', include(('store_products.urls', 'store_products'), namespace='store_products')),

    # ✅ ORDERS (THIS is what enables /orders/create/)
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),

    # Other apps
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # Admin
    path('admin/', admin.site.urls),
]

# Media during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)