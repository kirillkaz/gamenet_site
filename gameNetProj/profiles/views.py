from django.conf import settings
from django.contrib.auth import login, authenticate
from .forms import CustomRegisterForm, CustomAuthForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import User


@csrf_exempt
def register_auth(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm()
        auth_form = CustomAuthForm(request.POST)

        if 'email' in request.POST:
            register_form = CustomRegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                user.refresh_from_db()
                user.save()
                login(request, user)
                return HttpResponse(f'<h1>{user.login} Успех!</h1>')
        
        elif auth_form.is_valid():
            user = authenticate(login=auth_form.cleaned_data['login'], password=auth_form.cleaned_data['password'])
            if user is not None:
                login(request, user)

        else:
            register_form = CustomRegisterForm()
            auth_form = CustomAuthForm()
        
    else:
        register_form = CustomRegisterForm()
        auth_form = CustomAuthForm()

    context = {
        'register_form': register_form,
        'auth_form': auth_form,
    }
    return render(request, 'auth_register/register_auth.html', context=context)

def main_page_view(request):
    pass