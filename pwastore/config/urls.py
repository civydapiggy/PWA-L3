"""
URL configuration for pwastore.

Routes:
- ''          -> store_products.urls  (homepage)
- 'cart/'     -> cart.urls
- 'accounts/' -> accounts.urls + Django auth URLs
- 'admin/'    -> Django admin

Also serves user-uploaded media from /media/ for this demo.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    # Homepage / product catalog
    path(
        "",
        include(("store_products.urls", "store_products"), namespace="store_products"),
    ),

    # Cart
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),

    # Accounts (your app) + built-in auth (login/logout/password)
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
    path("accounts/", include("django.contrib.auth.urls")),

    # Admin
    path("admin/", admin.site.urls),
]

# --- Media files (uploaded images) ---
# DEBUG: use Django helper
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Non-DEBUG (Render demo): serve from disk via Django
else:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
