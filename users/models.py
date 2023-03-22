from django.db import models

from django.contrib.auth.models import AbstractUser   #готовый шаблон работы с юзером
# Create your models here.

class User(AbstractUser):  #наследуемся от абстракт юзер
    image = models.ImageField(upload_to='user_images', null=True, blank=True)  #к уже готовой модели конектим доп функции
