from django.conf import settings
from django.contrib.auth import login
from .forms import CustomRegisterForm, CustomAuthForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

@csrf_exempt
def register(request):
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


class UserLoginView(LoginView):
    template_name = 'auth_register/register_auth.html'
    form = CustomAuthForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
    
    def get_success_url(self):
        return reverse_lazy('register')