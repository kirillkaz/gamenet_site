from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

'''
временно - мусор
'''
# class CustomAuthForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'user_login','placeholder':'Логин'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'user_password','placeholder':'Пароль'}))


class CustomAuthForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class':'user_login','placeholder':'Логин', 'v-on:click': 'testFoo'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'user_password','placeholder':'Пароль'}))


class CustomRegisterForm(UserCreationForm):
    login = forms.CharField(widget=forms.TextInput(attrs={'class':'register_input','placeholder':'Логин'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'register_input','placeholder':'Электронная почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'register_input','placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'register_input','placeholder':'Подтверждение пароля'}))
    class Meta:
        model = User
        fields = ['login', 'email', 'password1', 'password2']


# class CustomAuthForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['login', 'password']