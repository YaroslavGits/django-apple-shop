from django.contrib import admin
from .models import *

# Register your models here.
class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

class DeliveryInOrderInline(admin.TabularInline):
    model = DeliveryInOrder
    extra = 1
    max_num = 1

class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order
    list_display = [fields.name for fields in Order._meta.fields]
    inlines = [DeliveryInOrderInline, ProductInOrderInline]


admin.site.register(Order, OrderAdmin)

class DeliveryAdmin(admin.ModelAdmin):
    class Meta:
        model = Delivery
    list_display = [fields.name for fields in Delivery._meta.fields]


admin.site.register(Delivery, DeliveryAdmin)

class StatusDeliveryAdmin(admin.ModelAdmin):
    class Meta:
        model = StatusDelivery
    list_display = [fields.name for fields in StatusDelivery._meta.fields]


admin.site.register(StatusDelivery, StatusDeliveryAdmin)

class StatusAdmin(admin.ModelAdmin):
    class Meta:
        model = Status
    list_display = [fields.name for fields in Status._meta.fields]


admin.site.register(Status, StatusAdmin)

class ProductInBasketAdmin(admin.ModelAdmin):
    class Meta:
        model = ProductInBasket
    list_display = [fields.name for fields in ProductInBasket._meta.fields]


admin.site.register(ProductInBasket, ProductInBasketAdmin)

# class StatusAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Status
#     list_display = [fields.name for fields in Status._meta.fields]
#
#
# admin.site.register(Status, StatusAdmin)