from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import ContactForm
from django.contrib.auth.models import User

# Create your views here.
def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    number = data.get("number", "1")
    is_delete = data.get("is_delete", 'false')
    print(product_id, number, is_delete)
    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).delete()
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, order__isnull=True, defaults={"number": number})
        if not created:
            new_product.number += int(number)
            new_product.save(force_update=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_number = products_in_basket.count()
    return_dict["products_total_number"] = products_total_number

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["number"] = item.number
        product_dict["price"] = item.price_all
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    delivery = Delivery.objects.filter(status_delivery_type=True)
    products_in_cart = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)

    return render(request, "orders/basket.html", locals())

def contact(request):
    session_key = request.session.session_key
    delivery = Delivery.objects.filter(status_delivery_type=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form =ContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        data = request.POST
        for name, value in data.items():
            if name.startswith('product_in_basket_'):
                product_in_basket_id = name.split('product_in_basket_')[1]
                product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)

                product_in_basket.number = value
                product_in_basket.save(force_update=True)
    return render(request, 'orders/Contacts.html', locals())

def payment(request):
    session_key = request.session.session_key
    delivery = Delivery.objects.filter(status_delivery_type=True)
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = ContactForm(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('yes')
            data = request.POST
            name = data['name']
            email = data['email']
            phone = data['phone']
            address = data['address']
            prices_for_delivery_type = data['delivery_type']
            for name, value in data.items():
                if name.startswith('delivery_type'):
                    price_for_delivery_type = value
            print(price_for_delivery_type)
            user, create = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            order = Order.objects.create(user=user, customer_name=name, customer_email=email, customer_number=phone,
                                         customer_address=address, status_id=1)
            deliverys = Delivery.objects.get(price_for_delivery_type=price_for_delivery_type)

            DeliveryInOrder.objects.create(order=order, delivery=deliverys)

            for product_in_basket in ProductInBasket.objects.filter(session_key=session_key, is_active=True,
                                                                    order__isnull=True):
                product_in_basket.order = order
                product_in_basket.save(force_update=True)

                ProductInOrder.objects.create(product=product_in_basket.product, number=product_in_basket.number,
                                              price_for_one=product_in_basket.price_for_one,
                                              price_all=product_in_basket.price_all, order=order)
        else:
            print('no')
    return render(request, 'orders/payment.html', locals())