from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from datetime import datetime


class UserManager(BaseUserManager):

    def create_user(self, login, password=None):
        if not login:
            raise ValueError('Users must have a login')

        user = self.model(
            login=login,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, login, password=None):

        user = self.create_user(
            login=login,
            password=password,
        )
        user.save(using=self._db)

        return user


'''
this modell created for users galaryes
'''
class UserImages(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('profiles.User', on_delete=models.CASCADE)
    image = models.ImageField()


'''
user of the gamenet
'''
class User(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = "login"
    login = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)

    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=14, blank=True)
    ''', unique=True'''
    #TODO сделать телефон каким то образом уникальным полем
    last_login = models.DateTimeField(default=datetime.now)

    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    
    avatar_id = models.IntegerField(default=0)
    galary = models.ManyToManyField(UserImages, related_name='images2users', blank=True)

    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)

    objects = UserManager()

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return True

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return True
    
    # def __str__():
    #     return self.login
    

'''
friends of the gamenet's user
'''
class User_Friends(models.Model):
    user_id = models.OneToOneField("User", on_delete=models.CASCADE, primary_key=True)
    friends = models.ManyToManyField(User, related_name='friends2users', blank=True)


'''
gamenet user's bio
'''
class Bio(models.Model):
    user_id = models.OneToOneField("User", on_delete=models.CASCADE, primary_key=True)
    user_description = models.CharField(max_length=250, blank=True)
    sex = models.CharField(max_length=1, blank=True)
    birthday = models.DateField(blank=True)