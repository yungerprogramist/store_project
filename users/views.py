from django.shortcuts import render , HttpResponsePermanentRedirect 
from django.urls import reverse #импортируем реверс и редирект для того что бы перенаправлять пользователя после регистрации

from users.forms import UserLoginForm, UserRegistrationForm,UserProfileForm #испортируем форму
from products.models import Basket 

from django.contrib.auth.decorators import login_required  #декоратор (подробнее во вьюхи продукта)
from django.contrib import auth, messages


# вход пользователя
def login (request):
    if request.method == 'POST': #если пришел пост запрос
        form = UserLoginForm(data = request.POST) #передаем данные из заполненный форм(из регистрации)
        if form.is_valid(): #проверка правильности данных (валидация)
            username = request.POST['username'] #если прошло валидацию то достаем из пост запроса (он является словарем) логин и пороль
            password = request.POST['password']
            #далее подтверждение. Есть ли такой пользователь в базе данных
            user = auth.authenticate (username = username, password = password) #так выглядит проверка по поролю и логину 
            if user: #если пользователя нашло в бд (то есть он есть)
                auth.login (request, user) #то его авторизует  
                return HttpResponsePermanentRedirect (reverse('products:index'))#перенаправление на главную страницу (так можно вернуть хоть куда)


    else :
        form =  UserLoginForm()
    context = {'form' : form}  #привязали форму к ключу для работы в html шаблоне
    return render (request, 'users/login.html', context)


# регистрация пользователя
def registration (request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save() # после валидации сохраняем его данные в бд
            messages.success(request, 'поздравляем, вы успешно зарегались')
            return HttpResponsePermanentRedirect (reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form' : form}
    return render (request, 'users/registration.html', context)

# from users.models import User
# User.objects.all() для просмотра всех зареганных юзеров

@login_required
def profile(request): 
    if request.method == 'POST':
        form = UserProfileForm(instance = request.user, data = request.POST, files = request.FILES) #ласт параметр отвечает за загрузку фотографии  
        if form.is_valid():
            form.save() # после валидации сохраняем его данные в бд
            return HttpResponsePermanentRedirect (reverse('users:profile'))
        else: 
            print(form.errors) #для понятия ошибок
    else:
        form   = UserProfileForm(instance = request.user)

    # baskets = Basket.objects.get() #теперь мы полностью взаимодействуем с классом из моделей products(фильтрация что бы у каждого юзера была своя корзина)

    # total_sum = sum([basket.sum() for basket in baskets]) #sum в данном случае встроенная функция питона 
    # total_quantity = sum([basket.quantity for basket in baskets])  все это оставил для примера, как можно прописать подсчет корзины

    # total_sum = 0
    # total_quantity = 0          корзина в лоб
    # for basket in baskets:
    #     total_sum += basket.sum()
    #     total_quantity += basket.quantity

    context = {
        'title': 'Store - профиль',
        'form':form ,
        'baskets': Basket.objects.all(),
        # 'total_sum': total_sum,
        # 'total_quantity': total_quantity,
        }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponsePermanentRedirect(reverse('products:index'))