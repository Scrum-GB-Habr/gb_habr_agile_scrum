import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
]