from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostsAPIView, news_page_view

app_name = 'activityApp'

urlpatterns = {
    path('api/v1/posts/<str:user_login>', PostsAPIView.as_view(), name='posts_api'),
    path('news', news_page_view, name='news_page'),
}
urlpatterns = format_suffix_patterns(urlpatterns)