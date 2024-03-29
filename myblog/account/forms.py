from django import forms
from django.contrib.auth.models import User
from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль 1',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Пароль 2',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли разные!')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['phone']
