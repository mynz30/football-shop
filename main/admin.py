from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'brand', 'rating')
    search_fields = ('name', 'category', 'brand')


# Register your models here.
