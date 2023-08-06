from django.db import models
from .platform_data import PLATFORM_NAMES
from profiles.models import User
'''
gamenet user's platforms
'''
class Platform(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, choices=PLATFORM_NAMES, default='Steam')
    image = models.CharField(blank=True)
    users = models.ManyToManyField(User, related_name='platform2users', blank=True)

# '''
# model for ManyToMany
# user >---< user_platforms
# '''
# class user_platforms(models.Model):
#     id = models.IntegerField(primary_key=True)
#     platform_id = models.ForeignKey('platform', on_delete=models.CASCADE)
#     user_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)

'''
links to user platforms
'''
class Platform_Link(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)
    platform_id = models.ForeignKey('platform', on_delete=models.CASCADE)
    link = models.CharField(blank=True)

# '''
# model for ManyToMany
# user >---< platform_link
# '''
# class platform_links(models.Model):
#     id = models.IntegerField(primary_key=True)
#     platform_link_id = models.ForeignKey('platform_link', on_delete=models.CASCADE)
#     user_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)