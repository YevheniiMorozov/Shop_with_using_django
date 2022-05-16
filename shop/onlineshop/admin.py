from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "category", "price", "remainder", "available", "created")
    search_fields = ("name", "category", "available")
    list_filters = ("category", "remainder", "available")
    list_editable = ("available", "price", "remainder")
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)