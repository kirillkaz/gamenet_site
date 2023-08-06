from django.db import models
from .abstractModels import Post, Comment
from datetime import datetime
from profiles.models import User


'''
this models was created for user's and group's posts
'''
class UserPosts(Post):
    TYPE_OF_CREATOR = 'profiles.User'

    creator_id = models.ForeignKey(f'{TYPE_OF_CREATOR}', on_delete=models.CASCADE)


class GroupPosts(Post):
    TYPE_OF_CREATOR = 'groups.Group'

    creator_id = models.ForeignKey(f'{TYPE_OF_CREATOR}', on_delete=models.CASCADE)


'''
this classes was created for comments to posts
'''
class GroupPostComment(Comment):
    TYPE_OF_COMMENT_POST = 'GroupPosts'

    post_id = models.ForeignKey(f'{TYPE_OF_COMMENT_POST}', on_delete=models.CASCADE)


class UserPostComment(Comment):
    TYPE_OF_COMMENT_POST = 'UserPosts'

    post_id = models.ForeignKey(f'{TYPE_OF_COMMENT_POST}', on_delete=models.CASCADE)


'''
this model was created for:
chats with many members
chats with two members
'''
class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    creator_id = models.ForeignKey('profiles.User', on_delete=models.PROTECT)
    avatar = models.CharField(blank=True)
    administrators = models.ManyToManyField(User, related_name='chat_admins2users')
    members = models.ManyToManyField(User, related_name='chat_membs2users')
'''
TODO сделать так, что бы при удалении акка овнера - овнером становился либо первый добавленный админ,
либо первый добавленный мембер (если в чате много пользователей)
'''

'''
this model was created for gamenet user's messages
'''
class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)
    chat_id = models.ForeignKey('Chat', on_delete=models.CASCADE)

    date = models.DateTimeField(datetime.now)
    text = models.CharField()
    is_viewed = models.BooleanField(default=False)

'''
TODO определиться с тем, что делать с сообщениями удаленных пользователей
А именно - как их сохранять так, что бы при создании нового пользователя и
возможного присвоения им айди старого пользователя - сообщение не становилось
сообщением нового пользователя
'''