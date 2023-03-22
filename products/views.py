from django.shortcuts import render , HttpResponseRedirect

from django.contrib.auth.decorators import login_required  #декоратор для исправления ошибок (пользователи которые не зарегались)

from products.models import Product , ProductCategory , Basket
from users.models import User

from django.core.paginator import Paginator #https://docs.djangoproject.com/en/4.1/ вот доки пагинатора

def index (request):
    context = {'title' : 'store'}
    return render(request , 'products/index.html', context)

def products (request, category_id = None, page_number = 1):  #передаем айди none но его может  и не быть
    
    # if category_id:  # если у нас есть id
    #     # category = ProductCategory.objects.get(id=category_id) # берем это id категорий
    #     # products = Product.objects.filter(category=category) # берем все продукты выбранной категории
    #     # следствие
    #     products = Product.objects.filter(category_id=category_id) # берем все продукты выбранной категории

    # else : #если у нас не выбранна(не пришла) id то беорем все продукты
    #     products = Product.objects.all()

    # можно все строчки превратить в одну

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()


    #пагинатор 

    per_page = 3
    paginator = Paginator(products, per_page ) #список пагинации (что пагинировать(продукты) количество товаров на странице)
    products_paginator = paginator.page(page_number)  #отвечает за страницы пагинации 


    context = {
        'title' : 'store - каталог',
        # 'products' : Product.objects.all(), убрал когда добавлял фильтрацию по категориям
        'categories' : ProductCategory.objects.all(),
        'products': products_paginator, #передаем пагинатор который включается в себя products
        }


    return render (request , 'products/products.html', context)

@login_required   #'''(login_url='/users/login/')''' перенаправление(оно стоит у нас в настройках так удобнее)  #декоратов
def basket_add (request , product_id):
    product = Product.objects.get(id=product_id)  #берем этот продукт на который кликнули что бы потом добавить в корзину
    baskets = Basket.objects.filter(user=request.user, product=product)  #фильтрация (просмотр есть ли у пользователя корзина, проверка есть ли у пользователя такой продукт)

    if not baskets.exists(): #если нету никаких обьектов в корзине она пустая
        Basket.objects.create(user = request.user , product=product, quantity = 1) #создаем этот товар в корзине (привязываем корзину к пользователю, загружаем продукт , количество = 1)
    else:
        basket = baskets.first()  # отфильтрованный элемен всегда будет первым
        basket.quantity +=1    #добавляем количетсво
        basket.save()

    return HttpResponseRedirect (request.META['HTTP_REFERER'])  #возвращает пользователя после нажатия кнопки на данную страницу 

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])