from django.shortcuts import render
from django.shortcuts import render_to_response
from .forms import SabscriberForm
from django.template import RequestContext
from products.models import Product, ProductImage, Category
# Create your views here.

def test(request):
    form = SabscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'land/test.html', locals())

def home(request):
    product_image = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category_id=2)[::-1]
    product_image = product_image[0:4]
    products_image = ProductImage.objects.filter(is_active=True, is_main=True , product__is_active=True)[::-1]
    products_image = products_image[0:4]
    category = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    return render(request, 'land/home.html', locals())

def about(request):
    return render(request, 'land/about.html', locals())