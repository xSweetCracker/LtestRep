from django.urls import path
from .views import user_login, register, edit

app_name = 'account'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit')
]
