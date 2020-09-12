from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'created', 'updated']
    list_filter = ['price', 'available', 'created', 'updated']
    list_editable = ['price']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
