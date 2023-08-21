from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import group_create_view, groups_page_view, GroupsAPIView

app_name = 'groups'

urlpatterns = {
    path('testgroup', group_create_view, name='register_auth'),
    path('groups', groups_page_view, name='groups_page'),
    path('api/v1/groups/<str:user_login>', GroupsAPIView.as_view(), name='groups_api'),
}
urlpatterns = format_suffix_patterns(urlpatterns)