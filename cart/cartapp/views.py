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




def show_cart(request):

    if "product_pk" in request.COOKIES:
        products_pk = products_pk.split(' ')
        
        list_products = list()
        for product_pk in products_pk:
            list_products.append(Product.objects.get(pk=product_pk))
        if request.method == 'POST':
            new_product = request.POST.get('product_pk')
            response.set_cookie('product_pk', new_product)
            list_products.pop(int(request.POST['product_pk'])) # Видаляємо товар зі списку за індексом
            new_product = ' '.join(str(product.pk) for product in list_products) # Створюємо новий рядок з PK товарів, які залишилися в кошику
            response = render(request, "cart.html", context={"products": list_products}) # Формуємо сторінку зі списком залишених товарів
            
            return response # Повертаємо сторінку зі списком залишених товарів
        else:
            response = render(request,"cart.html",context={"products": list_products})
    else:
        response = render(request,"cart.html",context={"products": []})
    return response



