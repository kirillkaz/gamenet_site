from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from datetime import date
# Create your models here.

class User(AbstractBaseUser):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    last_login = None

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    gamelist_id = models.IntegerField()
    avatar_id = models.IntegerField()

    is_superuser = False
    is_staff = False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_staff == True

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser == True
