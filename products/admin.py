from django.contrib import admin
from .models import Product, Category, Subcategory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'price',
        'rating',
        'stock_status',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'category',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)