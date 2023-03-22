from django.urls import path  
from . import views  #из этой же директории импорт файла views


app_name = 'products'

urlpatterns = [
    path('', views.index , name ='index'), 
    path('category/<category_id>/', views.products , name ='category'),  #подключение переброски товаров по категориям
    path('page/<int:page_number>/', views.products , name ='paginator'), #подключение пагинации

    path ('products', views.products, name = 'products'),#хз че вот это за строчка но без нее тут не работает нужно фиксить

    path('baskets/add/<int:product_id>/', views.basket_add,  name = 'basket_add'),   #int передаем ему значение параметра функции вьюха
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove')
]