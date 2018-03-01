from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length=32, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status Order: %s" % self.status_name
    class Meta():
        verbose_name = "Status Order"
        verbose_name_plural = "Status Orders"


class Delivery(models.Model):
    delivery_type = models.CharField(max_length=32, blank=True, null=True, default=None)
    status_delivery_type = models.BooleanField(default=True)
    price_for_delivery_type = models.IntegerField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Delivery: %s" % self.delivery_type
    class Meta():
        verbose_name = "Delivery"
        verbose_name_plural = "Delivery"


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    customer_name = models.CharField(max_length=100,blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_number = models.CharField(max_length=100, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=100, blank=True, null=True, default=None)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(Status, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Order: %s " % self.id

    class Meta():
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class StatusDelivery(models.Model):
    status_delivery_name= models.CharField(max_length=32,blank=True, null=True, default=None)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status Delivery: %s" % self.status_delivery_name
    class Meta():
        verbose_name = "Status Delivery"
        verbose_name_plural = "Status Delivery"


class DeliveryInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    delivery = models.ForeignKey(Delivery, blank=True, null=True, default=None)
    delivery_status = models.ForeignKey(StatusDelivery, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Delivery Type: %s" % self.delivery.delivery_type

    class Meta():
        verbose_name = "Delivery Product"
        verbose_name_plural = "Delivery Products"

    def save(self, *args, **kwargs):
        order = self.order
        total_price = 0
        for price in ProductInOrder.objects.filter(order=order, product_status=True):
            total_price += price.price_all
        delivery = self.delivery
        amount_price = total_price + delivery.price_for_delivery_type
        self.order.total_price = amount_price
        self.order.save(force_update=True)
        super(DeliveryInOrder, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product_status = models.BooleanField(default=True)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    price_for_one = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    number = models.IntegerField(blank=True, null=True, default=1)
    price_all = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Selected Product: %s" % self.product.name

    class Meta():
        verbose_name = "Selected Product"
        verbose_name_plural = "Selected Products"

    def save(self, *args, **kwargs):
        self.price_for_one = self.product.discount_price
        self.price_all = self.price_for_one * self.number
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_oder_post_save(sender, instance, created, **kwargs):
    order = instance.order
    total_price = 0
    for price in ProductInOrder.objects.filter(order=order, product_status=True):
        total_price += price.price_all
    delivery_in_order = DeliveryInOrder.objects.get(order=order)
    amount_price = total_price + delivery_in_order.delivery.price_for_delivery_type
    instance.order.total_price = amount_price
    instance.order.save(force_update=True)
post_save.connect(product_in_oder_post_save, sender=ProductInOrder)

class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    price_for_one = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    number = models.IntegerField(blank=True, null=True, default=1)
    price_all = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Selected Product: %s" % self.product.name
    class Meta():
        verbose_name = "Product In Basket"
        verbose_name_plural = "Products In Basket"

    def save(self, *args, **kwargs):
        self.price_for_one = float(self.product.discount_price)
        self.price_all = self.price_for_one * int(self.number)
        super(ProductInBasket, self).save(*args, **kwargs)

# def delivery_in_order_save(sender, instance, created, **kwargs):
#     order = instance.order
#     total_price = 0
#     for price in ProductInOrder.objects.filter(order=order, product_status=True):
#         total_price += price.price_all
#     delivery = instance.delivery
#     delivery_in_order = DeliveryInOrder.objects.get(order=order, delivery=delivery)
#     amount_price = total_price + delivery_in_order.delivery.price_for_delivery_type
#     instance.order.total_price = amount_price
#     instance.order.save(force_update=True)
# post_save.connect(delivery_in_order_save, sender=DeliveryInOrder)

