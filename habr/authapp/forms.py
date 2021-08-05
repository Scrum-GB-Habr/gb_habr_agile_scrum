from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UserChangeForm, PasswordChangeForm
from .models import AuthorizedUser


class AuthorizedLoginUser(AuthenticationForm):
    """
    Форма авторизации
    """
    class Meta:
        model = AuthorizedUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(AuthorizedLoginUser, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации
    """
    class Meta:
        model = AuthorizedUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class UserEditProfile(UserChangeForm):
    """
    Форма редактирования профиля
    """
    class Meta:
        model = AuthorizedUser
        fields = (
            'username',
            'first_name',
            'email',
            'age',
            'about_me',
            'gender',
            'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class UserPasswordForm(PasswordChangeForm):
    """
    Форма смены пароля
    """
    class Meta:
        model = AuthorizedUser
        fields = ('password', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
