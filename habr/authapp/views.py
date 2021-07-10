from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import AuthorizedLoginUser, UserRegisterForm, UserEditPrifile

from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login(request):
    title = 'Log In'

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
    title = 'Sign Up'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def edit(request): # чтобы можно было редактировать профиль
    title = 'Profile'

    if request.method == 'POST':
        edit_form = UserEditPrifile(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditPrifile(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)


