# pwastore/store_products/apps.py
from django.apps import AppConfig

class StoreProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store_products"   # <-- NOT "pwastore.store_products"
