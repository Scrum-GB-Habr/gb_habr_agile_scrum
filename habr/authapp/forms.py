from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import AuthorizedUser

class AuthorizedLoginUser(AuthenticationForm): # форма авторизации
    class Meta:
        model = AuthorizedUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AuthorizedLoginUser, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm): # регистрация
    class Meta:
        model = AuthorizedUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

