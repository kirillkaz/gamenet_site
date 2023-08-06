from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import signup
urlpatterns = {
    path('auth', signup, name='auth'),
}
urlpatterns = format_suffix_patterns(urlpatterns)#