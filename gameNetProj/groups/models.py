from django.db import models
from profiles.models import User

'''
this model created for groups in gamenet
'''
class Group(models.Model):
    id = models.IntegerField(primary_key=True)

    owner_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='groups2users', default=None)

    name = models.CharField(100, default=None)
    avatar = models.CharField(default=None)
    description = models.CharField(100, default=None)

    is_private = models.BooleanField(default=False)
    

#TODO определиться с тем, что делать с группой, если админ удаляет свой акк


