from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import register_auth
urlpatterns = {
    path('register', register_auth, name='register'),
#    path('auth', register_auth.as_view(), name='auth'),
}
urlpatterns = format_suffix_patterns(urlpatterns)#