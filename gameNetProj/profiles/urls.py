from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import register_auth, main_page_view
urlpatterns = {
    path('register', register_auth, name='register_auth'),
    path('news', main_page_view, name='main_page'),
}
urlpatterns = format_suffix_patterns(urlpatterns)