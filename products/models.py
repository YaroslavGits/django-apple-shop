from django.db import models
from django.db.models.signals import post_save

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    category_image = models.ImageField(upload_to='category_image/')
    category_url = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Category: %s" % self.category_name
    class Meta():
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None)
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.FloatField(blank=True, null=True, default=0)
    discount = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Product: %s" % self.name
    class Meta():
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_image/')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Product Image: %s" % self.id
    class Meta():
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


def product_post_save(sender, instance, created, **kwargs):
    discount = instance.discount
    price = instance.price
    discount_price = price - ((price * discount) / 100)
    print(price)
    instance.discount_price = discount_price
    instance.save(force_update=True)
post_save.connect(product_post_save, sender=Product)