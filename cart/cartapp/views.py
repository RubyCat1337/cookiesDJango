from django.shortcuts import render, redirect
from django.http import JsonResponse
from cartapp.models import *
from django.http import HttpResponse
# Create your views here.
def show_products(request):
    #Відобразіть шаблон products.html з усіма об’єктами Product
    response = render(request,"products.html",context={"products": Product.objects.all()})
    #метод запиту POST
    if request.method == "POST":
        if "product_pk" not in request.COOKIES: #Якщо в запиті немає файлу cookie 'product_pk'
            new_product = request.POST.get('product_pk') #Отримуем product_pk запиту POST
            response.set_cookie('product_pk',new_product) #Встановлюе cookie 'product_pk' зі значенням new_product
            return response #Повернути 
        else: #Якщо в запиті є файл cookie 'product_pk'
            #об'єднайе його з новим product_pk 
            new_product = request.COOKIES['product_pk'] + " " + request.POST.get('product_pk') # "1" + " " + "2"  = "1 2"
            response.set_cookie('product_pk',new_product) ##Встановлюе cookie 'product_pk' зі значенням new_product
            return response 

    return response




#Розумні речі приходить коли опломником по голові б'ють
def show_cart(request):
    products_pk = request.COOKIES.get('product_pk', '').split()
    list_products = Product.objects.filter(pk__in=products_pk)
    response = render(request, 'cart.html', {'products': list_products})

    if request.method == 'POST':
        pk_deleted = request.POST.get('product_pk')
        if pk_deleted:
            products_pk.remove(pk_deleted)
            new_product = ' '.join(products_pk)
            if new_product:
                list_products = Product.objects.filter(pk__in=products_pk)
                response = render(request, 'cart.html', {'products': list_products})
                response.set_cookie('product_pk', new_product)
            else:
                response = render(request, 'cart.html', {'products': []})
                response.delete_cookie('product_pk')

    return response


