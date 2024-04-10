from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "product_name",
        "price",
        "available",
        "created_at",
        "updated_at",
    ]
    list_filter = ["available", "created_at", "updated_at"]
    list_editable = ["price", "available"]


admin.site.register(Product, ProductAdmin)
