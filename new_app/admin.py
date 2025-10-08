from django.contrib import admin
from .models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'photo', 'category', 'price', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)




