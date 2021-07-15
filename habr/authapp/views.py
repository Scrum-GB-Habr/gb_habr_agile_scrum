from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import AuthorizedLoginUser, UserRegisterForm, UserEditProfile, UserPasswordForm

from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def login(request):
    title = 'Войти'

    login_form = AuthorizedLoginUser(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('mainapp:home'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:home'))


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


@login_required
def edit(request):  # чтобы можно было редактировать профиль
    title = 'Профиль'

    if request.method == 'POST':
        edit_form = UserEditProfile(
            request.POST,
            request.FILES,
            instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditProfile(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)


@login_required
def change_password(request):  # смена пароля пользователя
    title = 'Изменить пароль'
    if request.method == 'POST':
        password_form = UserPasswordForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            # меняем пароль в сессии, чтобы не вводить заново
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('auth:edit'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        password_form = UserPasswordForm(request.user)

    content = {'title': title, 'password_form': password_form}
    return render(request, 'authapp/change_password.html', content)
