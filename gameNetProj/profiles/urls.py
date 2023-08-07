from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import register, UserLoginView
urlpatterns = {
    path('register', register, name='register'),
    path('auth', UserLoginView.as_view(), name='auth'),
}
urlpatterns = format_suffix_patterns(urlpatterns)#