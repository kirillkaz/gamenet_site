import os
from io import BytesIO
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import boto3
import boto3.s3 as bs3
from botocore.client import Config
import base64

from django.shortcuts import render, HttpResponse
from .forms import GroupForm
from .models import Group
from django.views.decorators.csrf import csrf_exempt
from profiles.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import GroupSerializer

class GroupsAPIView(APIView):
    def get(self, request, user_login):
        user_groups = Group.objects.filter(subscribers__login=user_login)
        return Response({'groups': GroupSerializer(user_groups, many=True).data})

#почти работает(картинки не загружаются)
@csrf_exempt
def group_create_view(request):
    error = ''

    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)

        if form.is_valid():

            try:
                user = User.objects.get(login=request.user.login)
                new_group = Group.objects.create(owner_id=user)

                new_group.owner_id = user
                new_group.name = form.cleaned_data.get('name')
                new_group.description = form.cleaned_data.get('description')
                new_group.is_private = form.cleaned_data.get('is_private')
                new_group.avatar = form.cleaned_data.get('avatar')

                # raw_subscribers = form.cleaned_data.get('subscribers')
                # group_subscribers = User.objects.filter(login__in=raw_subscribers)
                # new_group.subscribers.set(group_subscribers)

                new_group.save()

                return HttpResponse(f'<h1>Успех!</h1>')
            
            except:
                error = 'Ошибка обработки формы!'
                return HttpResponse(f'<h1>{error}</h1>')
            
        else:
            error = 'Форма то инвалидна, сынок'
    else:
        form = GroupForm()

    context = {
        'form': form,
        'err': error
    }

    return render(request, 'testpages/test_page.html', context)


def groups_page_view(request):


    s3 = boto3.resource('s3',
                        endpoint_url='http://s3:9000',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                        config=Config(signature_version='s3v4'),
                        region_name='eu-west-1')
    buf = BytesIO()
    s3.Bucket('media-bucket').download_fileobj('snake.png', buf)
    
    context  = {'bytes': base64.b64encode(buf.getvalue()).decode('utf-8')}
    return render(request, 'groups_page.html', context)
