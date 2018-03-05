from django.shortcuts import render
from django.shortcuts import render_to_response
from products.models import *
from orders.models import *
# Create your views here.

def product(request, product_id):
    products = Product.objects.get(id=product_id)
    main_image = ProductImage.objects.filter(product=products)
    delivery = Delivery.objects.filter(status_delivery_type=True)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()


    return render(request, 'products/product.html', locals())

def laptop(request):
    product_image = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category_id=1)
    category = Category.objects.get(id=1)
    category_list = Category.objects.filter(is_active=True)
    return render(request, 'products/category.html', locals())

def iphone(request):
    product_image = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category_id=2)
    category = Category.objects.get(id=2)
    category_list = Category.objects.filter(is_active=True)
    return render(request, 'products/category.html', locals())

def ipad(request):
    product_image = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category_id=3)
    category = Category.objects.get(id=3)
    category_list = Category.objects.filter(is_active=True)
    return render(request, 'products/category.html', locals())

def imac(request):
    product_image = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category_id=4)
    category = Category.objects.get(id=4)
    category_list = Category.objects.filter(is_active=True)
    return render(request, 'products/category.html', locals())