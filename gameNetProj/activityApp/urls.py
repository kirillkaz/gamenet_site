from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostsAPIView, news_page_view, post_form_ajax, comment_form_ajax

app_name = 'activityApp'

urlpatterns = {
    path('api/v1/posts/<str:user_login>', PostsAPIView.as_view(), name='posts_api'),
    path('news', news_page_view, name='news_page'),
    path('activities/users/posts', post_form_ajax, name='create_post_ajax'),
    path('activities/users/comments/<int:post_id>', comment_form_ajax, name='create_comment_ajax'),
}
urlpatterns = format_suffix_patterns(urlpatterns)