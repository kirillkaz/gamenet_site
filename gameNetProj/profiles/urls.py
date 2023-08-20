from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import register_auth

urlpatterns = {
    path('register', register_auth, name='register_auth'),
}
urlpatterns = format_suffix_patterns(urlpatterns)