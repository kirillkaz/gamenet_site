from django.db import models
from datetime import datetime


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=datetime.now)
    text = models.CharField(default=None)
    published = models.BooleanField(default=False)

    #TODO добавить количество просмотров (щас я хз как это сделать)

    class Meta:
        abstract = True
        ordering = ['-date',]


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)
    text = models.CharField(default=None)
    date = models.DateTimeField(default=datetime.now)

    class Meta:
        abstract = True
        ordering = ['-date',]

'''
TODO определиться с тем, что делать с комментами удаленных пользователей
А именно - как их сохранять так, что бы при создании нового пользователя и
возможного присвоения им айди старого пользователя - коммент не становился
комментом нового пользователя
'''