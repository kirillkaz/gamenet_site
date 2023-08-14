from django.contrib import admin
from .models import User, Bio, User_Friends, UserImages

admin.site.register(User)
admin.site.register(Bio)
admin.site.register(User_Friends)
admin.site.register(UserImages)
# Register your models here.
