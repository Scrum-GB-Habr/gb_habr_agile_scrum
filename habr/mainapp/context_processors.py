from django.db.models import Q, F
from django.contrib.auth.models import User, Group

from .models import Category

def my_main_menu(request):
    print("context processor my_main_menu works")
    my_main_menu = []
    my_main_menu = Category.objects.all()
    print(my_main_menu.query)

    return {
        "my_main_menu": my_main_menu,
    }
