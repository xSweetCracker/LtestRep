from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView

from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegisterForm


# Create your views here.
def user_login(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(
                        request,
                        'account/profile.html'
                    )
                else:
                    return HttpResponse('Не активный!')

            else:
                return HttpResponse('Неверные данные!')

    else:
        form = LoginForm()

    return render(
        request,
        'account/login.html',
        {'form': form}
    )


def register(request: HttpRequest, *args, **kwargs):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(
                request,
                'account/profile.html'
            )

    else:
        user_form = UserRegisterForm()

    return render(
        request,
        'account/register.html',
        {'user_form': user_form}
    )


def out(request: HttpRequest):
    pass
