from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import register_auth,\
      profiles_page,\
      profile_menu_ajax,\
      profile_settings_ajax,\
      settings_page,\
      user_posts_ajax,\
      user_show_comments_ajax

urlpatterns = {
    path('register', register_auth, name='register_auth'),
    path('profiles/<str:username>', profiles_page, name='profiles_page'),
    path('profiles/ajax/menu', profile_menu_ajax, name='menu_ajax'),
    path('profiles/ajax/settings/profile', profile_settings_ajax, name='settings_profile_ajax'),
    path('profiles/ajax/posts/<str:username>', user_posts_ajax, name='user_posts_ajax'),
    path('profiles/ajax/comments/<int:post_id>', user_show_comments_ajax, name='comments_ajax'),
    path('profile/settings', settings_page, name='settings'),
}
urlpatterns = format_suffix_patterns(urlpatterns)