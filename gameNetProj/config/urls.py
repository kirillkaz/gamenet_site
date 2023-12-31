from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    # path('api-auth', include('rest_framework.urls')),
    # path('auth', include('djoser.urls')),
    path('', include('profiles.urls')),
    path('', include('activityApp.urls')),
    path('', include('groups.urls'))
    #path('auth', include('djoser.urls.jwt')),
] + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
