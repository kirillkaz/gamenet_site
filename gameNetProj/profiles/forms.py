from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, UserImages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class CustomAuthForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={'class':'user_login','placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'user_password','placeholder':'Пароль'}))


class CustomRegisterForm(UserCreationForm):
    login = forms.CharField(widget=forms.TextInput(attrs={'class':'register_input','placeholder':'Логин'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'register_input','placeholder':'Электронная почта'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'register_input','placeholder':'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'register_input','placeholder':'Подтверждение пароля'}))
    class Meta:
        model = User
        fields = ['login', 'email', 'password1', 'password2']


class UserImagesForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'image_input', 'accept': 'image/', 'onchange': 'download(this)'}))
    
    class Meta:
        model = UserImages
        fields = ['image']
