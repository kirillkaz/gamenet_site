from django.conf import settings
from django.contrib.auth import login
from .forms import CustomRegisterForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            login(request, user)

            return HttpResponse(f'<h1>{user.login} Успех!</h1>')
        else:
            form = CustomRegisterForm()

    else:
        form = CustomRegisterForm()  
    return render(request, 'auth_register/register_auth.html', {'form': form})