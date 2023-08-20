from django.db import models
from profiles.models import User
from django_minio_backend import MinioBackend, iso_date_prefix
from config.settings import DEFAULT_FILE_STORAGE
'''
this model created for groups in gamenet
'''
class Group(models.Model):
    id = models.AutoField(primary_key=True)

    owner_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='groups2users', blank=True)

    name = models.CharField(100, blank=True)
    avatar = models.ImageField(blank=True)
    
    description = models.CharField(100, blank=True)

    is_private = models.BooleanField(default=False)
    

#TODO определиться с тем, что делать с группой, если админ удаляет свой акк


