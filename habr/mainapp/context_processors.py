from django.db.models import Q, F
from django.contrib.auth.models import User, Group

from .models import Category, Post


def my_main_menu(request):
    # print("context processor my_main_menu works")
    # my_main_menu = []
    my_main_menu = Category.objects.filter(post__is_active=True, post__published=True).distinct()
    on_modering_cnt = Post.objects.filter(is_active=True, on_moderation=True).count()
    # print(my_main_menu.query)

    return {
        "my_main_menu": my_main_menu,
        "on_modering_cnt": on_modering_cnt
    }
