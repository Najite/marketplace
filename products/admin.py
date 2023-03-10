from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['seller', 'name', 'price', 'category']
    list_filter = ['price', 'category']
    
    

