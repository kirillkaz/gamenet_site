from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from .models import User

class CustomAuthForm(AuthenticationForm):
    login = forms.CharField(widget=forms.TextInput(attrs={'class':'user_login','placeholder':'Логин'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'user_login','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'user_password','placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'user_password','placeholder':'Подтверждение пароля'}))

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['login', 'email', 'password1', 'password2']