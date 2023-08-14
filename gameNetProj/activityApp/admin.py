from django.contrib import admin
from .models import UserPosts, GroupPosts, GroupPostComment, UserPostComment, Chat, Message

admin.site.register(UserPosts)
admin.site.register(UserPostComment)
admin.site.register(GroupPosts)
admin.site.register(GroupPostComment)
admin.site.register(Chat)
admin.site.register(Message)
# Register your models here.
