from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "primaryCategory")
    list_editable = ("primaryCategory",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "featured")
    list_filter = ("category", "featured")
    list_editable = ("featured",)
    search_fields = ("name",)