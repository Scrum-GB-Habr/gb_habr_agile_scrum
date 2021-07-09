from django import forms
from django.utils.translation import gettext_lazy as t
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UsernameField,
)
from . import models

class RegisterUserForm(UserCreationForm):
    email = forms.CharField(
        label=t('Email'),
        widget=forms.EmailInput(
            attrs={"class": 'form-control', 'placeholder': t('Email'), 'required': True}
        ),
    )

    nickname = forms.RegexField(
        label='Nickname',
        max_length=50,
        regex=r'^[\w.@+-]+$',
        help_text=t(
            'Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'
        ),
        error_messages={
            'invalid': t(
                'This value may contain only letters, numbers and @/./+/-/_ characters.'
            )
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'nickname',
                'required': 'true',
            }
        ),
    )

    password1 = forms.CharField(
        label=t('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': t('password'),
                'required': True,
            }
        ),
    )

    password2 = forms.CharField(
        label=t('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': t('password confirmation'),
                'required': True,
            }
        ),
    )

    class Meta:
        model = models.User

        fields = [
            'email',
            'nickname',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

        def clean_password(self):
            cleaned_data = self.cleaned_data
            if cleaned_data['password2'] != cleaned_data['password']:
                raise ValidationError(t('Password dont match'))
            return cleaned_data['password2']


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        label=t('Email'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autofocus': True,
                'placeholder': t('email'),
            }
        ),
        error_messages={
            'required': t('Please enter your email'),
            'invalid': t('Please enter your email valid'),
        },
    )

    password = forms.CharField(
        label=t('Password'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': t('password')}
        ),
        error_messages={
            'required': t('Please enter your password'),
            'invalid': t('Please enter your password valid'),
        },
    )

    remember_me = forms.BooleanField(label=t('Remember Me'), required=False)