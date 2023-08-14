from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostsAPIView
urlpatterns = {
    path('api/v1/<str:user_login>', PostsAPIView.as_view(), name='register_auth'),
}
urlpatterns = format_suffix_patterns(urlpatterns)