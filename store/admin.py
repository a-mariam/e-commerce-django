from django.contrib import admin

from store.models import Product, Collection


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'last_update']
    list_per_page = 10
    prepopulated_fields = {'slug': ['title']}
    search_fields = ['title']
    ordering = ['-title']


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10



