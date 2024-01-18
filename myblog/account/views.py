from django.shortcuts import render
from django.views.generic import CreateView

from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


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
                    return HttpResponse('Successfully')
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
