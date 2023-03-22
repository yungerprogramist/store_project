#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


# django-admin startproject taskmanager для вызова создания этой папки со всеми всттроенными файлами
# ./manage.py startapp products      - для создания приложения

# python manage.py startapp main  для создания нового приложения(файла,страницы) после создания не забудь добавить фаил в "installed_app" в "setting.py" (зарегестрировать)

# python manage.py runserver для запуска интернет страницы , если не работает в терминале укажи путь до taskmanager  (через cd)
# ctrl + c  для выхода из запущенного сервера

# при введении admin возникает окошко входа, что бы его заполнить нужно сначало зарегаться . Для этого : 1. в терминале прописать (python manage.py createsuperuser) 2.ввести данные - имя пользователя, почта(необязательно), пароль, повтор пароля (если говорит что пароль простой введи "y")

# python manage.py shell



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
