from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import group_create_view
urlpatterns = {
    path('testgroup', group_create_view, name='register_auth'),
}
urlpatterns = format_suffix_patterns(urlpatterns)