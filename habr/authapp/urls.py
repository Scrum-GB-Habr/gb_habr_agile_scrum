from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    # чтобы можно было редактировать профиль
    path('edit/', authapp.edit, name='edit'),
    path('password/', authapp.change_password, name='change_password'),
]
