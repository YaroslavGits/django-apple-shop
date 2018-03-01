from django.contrib import admin
from .models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    list_display = [fields.name for fields in Product._meta.fields]
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
    list_display = [fields.name for fields in Category._meta.fields]

admin.site.register(Category, CategoryAdmin)
# class ProductImageAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Product
#     list_display = [fields.name for fields in ProductImage._meta.fields]
#
# admin.site.register(ProductImage, ProductImageAdmin)