
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserChangeForm #импорт уже готового шаблона авторизации и регистрации
from users.models import User

from django import forms #пакет для стилей формы

class UserLoginForm (AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',   #указываем какой класс из html шаблона прикрутить (берем его от input)
        'placeholder' : 'Введите имя пользователя'
    })) #кастомизируем поля ввода (указываем какой input(под почту или под текст и тд) и подключаем классы из html файла и плэйхолдер (в моем случае только плэйхолдер))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'введите пароль'
    }))

    class Meta:  #класс помогает определить модели с какими полями он будет работать (куда отправлять полученные данные и с чем связывать)
        model = User #в данном случае этот класс будет работать с моделью пользователей (из users.models)
        fields = ('username', 'password') #а конкретно с такими полями

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'введите имя'
    })) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'введите фамилию'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'введите имя пользователя'
    })) 
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'введите почту'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'введите пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'подтвердите пароль'
    }))
    
    
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username','email','password1', 'password2' )


class UserProfileForm (UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
    })) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : 'custom-file-input',
    }), required=False) #не обязательно для заполнения
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4', 
        'readonly' : True #это значит что текст можно будет только смотреть, но не редактировать
    })) 
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : 'form-control py-4',
        'readonly' : True
    }))

    class Meta :
        model = User
        fields = ('first_name', 'last_name', 'image', 'username','email')