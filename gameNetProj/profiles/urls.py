from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import register_auth, profiles_page, profile_menu_ajax

urlpatterns = {
    path('register', register_auth, name='register_auth'),
    path('profiles/<str:username>', profiles_page, name='profiles_page'),
    path('profiles/ajax/menu', profile_menu_ajax, name='menu_ajax')
}
urlpatterns = format_suffix_patterns(urlpatterns)