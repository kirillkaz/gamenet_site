from django.conf import settings
from django.contrib.auth import login, authenticate
from .forms import CustomRegisterForm, CustomAuthForm
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from .models import User
from django.http import JsonResponse, HttpResponseBadRequest


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
                return redirect(reverse('activityApp:news_page'))
        
        elif auth_form.is_valid():
            user = authenticate(login=auth_form.cleaned_data['login'], password=auth_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('activityApp:news_page'))

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


def profiles_page(request, username):
    context = {}
    return render(request, 'profiles/profiles.html', context=context)


def profile_menu_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            context = {}
            return render(request, 'ajax/profiles_ajax.html', context)
        else:
            return JsonResponse({'req_error': 'invalid request'}, status=400)
        
    else:
        return HttpResponseBadRequest('Invalid request')
