from django.db import models

from users.models import User  #для корзины

# Create your models here.

# python manage.py makemigrations -для создания миграции всех конструкции

# python manage.py migrate  для миграции созданных конструкции

# https://docs.djangoproject.com/en/4.1/ref/models/querysets/  - queryset api reference для работы с бд (5 модуль)
# https://docs.djangoproject.com/en/4.1/ref/models/fields/  документация для создания полей заполнения




class ProductCategory (models.Model):
    name = models.CharField(max_length=128, unique= True) #CharField - это строковое поле для строк малого и большого размера (максимум указываем сами , уникальность названия)
    description = models.TextField(null=True , blank=True) #TexrField для бол кол-во текста (поле может быть пустым)

    def __str__ (self):
        return self.name #выводим информацию об обьекте в виде названия переданной name (мы переписываем модуль)

class Product (models.Model):
    name = models.CharField (max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6 , decimal_places=2) #для работы с ценами (сколько цифр до и после запятой)
    quantity = models.PositiveIntegerField(default= 0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to= ProductCategory, on_delete= models.CASCADE) #к какой категории относится продукт (связываем нашу модель с другим классом, cascade - предупреждает об удалении всего в категории в случае попытки ее удаления  protect - не удалит пока категория не будет пустой )

    def __str__ (self):
        return f'продукт: {self.name} / категория : {self.category.name}'
    

class BasketQuerySet(models.QuerySet):  #для подсчетов корзины(наследуемся от квери сета в котором уже есть baskets(мы передали его) в self)
    def total_sum(self):  
        return sum(basket.sum() for basket in self)
     
    def total_qantity(self):
        return sum(basket.quantity for basket in self)
    
class Basket(models.Model):
    user = models.ForeignKey(to=User , on_delete=models.CASCADE) #привязываемся к пользователю
    product = models.ForeignKey(to=Product , on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)  #количество товаров в корзине
    created_timestamp = models.DateTimeField(auto_now_add=True) #отвечает за отображение времени (заполняется автоматически при создании нового обьекта) 

    objects = BasketQuerySet.as_manager()    #вот эта строчка перенапрвяляет инфу от baskets в другой класс

    def __str__(self):
        return f'корзина для {self.user.username} / Продукт: {self.product.name}' 
    
    def sum(self):
        return self.product.price*self.quantity

    # def total_sum(self):
    #     baskets = Basket.objects.get(user=self.user) # я взял тут get но в курсе было filter(он не работал)
    #     return sum(basket.sum() for basket in baskets)
    
    # def total_qantity(self):
    #     baskets = Basket.objects.get(user=self.user)
    #     return sum(basket.quantity for basket in baskets)


# работа с консолью

# (добавление элементов в таблицу):
# from products.models import ProductCategory
# category = ProductCategory (name = 'одежда', description = 'описание для одежды')
# category.save()
# category - выведет нам значения этой переменной
# category = ProductCategory.objects.get(id =1) - выводит название обьекта .all - всю бызу данных этого класса
# category -не забудь прописать это

# category.objects.create(name = 'лазанья') - один из вариантов добавления (быстрый)
# category.objects.filter(discription = None) - фидьтр обьекты (у которых нет описание в данном случае)'

# всю инфу по shell можно найти загуглив - django all


# выводит список элементов
# from products.models import eat
# eating = eat.objects.all()
# for eat in eating:
#     print(eating)

# https://docs.djangoproject.com/en/4.1/ref/models/querysets/ - для работы с shell


# выводим фикстуру - она нужна для сохранения базы данных в случае удаления :
# ./manage.py dumpdata products.eat > eatss.json  (указываем что хотим сохранить, какой тип файла и по желанию путь)
# создаем папку fixtures в products и перекидываем туда созданные фикстуры
# что бы загрузить все значения базы данных:
# ./manage.py loaddata /путь от store до json файлов

