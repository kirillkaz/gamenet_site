from io import BytesIO
from config.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import boto3
from botocore.client import Config
import base64

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import GroupForm
from .models import Group
from profiles.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GroupSerializer

from tools.load_avatar import LoadUserAvatar
from tools.ajax_wrapper import get_ajax_wrapper

class GroupsAPIView(APIView):
    def get(self, request, user_login):
        user_groups = Group.objects.filter(subscribers__login=user_login)
        return Response({'groups': GroupSerializer(user_groups, many=True).data})
    

def get_groups_context(request, p_type:str, client_type:str):
    '''
    This function get groups by usertype and client type in group
    in usertype:
    subscriber - get groups where user is subscriber
    admin - get groups where user is administrator

    in client type:

    client - user

    ajax - ajax
    '''
    #get current user login
    login = request.user.login

    #get grupst by usertype in groups
    if p_type == 'subscriber':
        user_groups = Group.objects.filter(subscribers__login=login)
        json_groups = GroupSerializer(user_groups, many=True).data

    elif p_type == 'admin':
        user = User.objects.get(login=login)
        user_groups = Group.objects.filter(owner_id=login)
        json_groups = GroupSerializer(user_groups, many=True).data

    #array for returm
    cleaned_groups = []

    #connection to minio database
    s3 = boto3.resource('s3',
                            endpoint_url='http://s3:9000',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            config=Config(signature_version='s3v4'),
                            region_name='eu-west-1')

    #class for context
    class cleaned_group:
                def __init__(self, g_name, g_avatar, g_subscribers):
                    self.name = g_name
                    self.avatar = g_avatar
                    self.subscribers = g_subscribers

    #filling context
    if client_type == 'client':
        for json_g in json_groups:
                buf = BytesIO()
                s3.Bucket('media-bucket').download_fileobj(json_g['avatar_name'], buf)
                cleaned_img = base64.b64encode(buf.getvalue()).decode('utf-8')

                cleaned_groups.append(cleaned_group(
                    g_name=json_g['name'],
                    g_avatar=cleaned_img,
                    g_subscribers=json_g['subscribers_count']))
                
    elif client_type == 'ajax':
        for json_g in json_groups:
                buf = BytesIO()
                s3.Bucket('media-bucket').download_fileobj(json_g['avatar_name'], buf)
                cleaned_img = base64.b64encode(buf.getvalue()).decode('utf-8')

                cleaned_groups.append({
                     'name': json_g['name'],
                     'avatar': cleaned_img,
                     'subscribers': json_g['subscribers_count'],
                })
    
    return cleaned_groups


@csrf_exempt
def groups_page_view(request):
    username = request.user.login
    user_avatar = LoadUserAvatar(username)

    cleaned_groups = get_groups_context(request, 'subscriber', 'client')
    context  = {'groups': cleaned_groups, 'user_avatar': user_avatar}
    return render(request, 'groups_page.html', context)


def create_group(request):
    form=GroupForm(request.POST, request.FILES)

    if form.is_valid():
        user = User.objects.get(login=request.user.login)
        new_group = Group.objects.create(owner_id=user)

        new_group.owner_id = user
        new_group.name = form.cleaned_data.get('name')
        new_group.description = form.cleaned_data.get('description')
        new_group.avatar = form.cleaned_data.get('avatar')
        new_group.subscribers.add(user)

        # raw_subscribers = form.cleaned_data.get('subscribers')
        # group_subscribers = User.objects.filter(login__in=raw_subscribers)
        # new_group.subscribers.set(group_subscribers)
        new_group.save()
    

def get_subscribed_groups(request):
    context = get_groups_context(request, 'subscriber', 'ajax')

    return get_ajax_wrapper(request=request, context=context, return_type='json')


def get_administrate_groups(request):
    context = get_groups_context(request, 'admin', 'ajax')

    return get_ajax_wrapper(request=request, context=context, return_type='json')
    

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
                new_group.avatar = form.cleaned_data.get('avatar')

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


def group_create_page(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            form = GroupForm()
            context = {'form': form}

            return render(request, 'ajax/groupCreationPage.html', context)
        
        elif request.method == 'POST':
            create_group(request)

        return JsonResponse({}, status=200)
    else:
        form = GroupForm()
        context = {'form': form}

        # return render(request, 'ajax/groupCreationPage.html', context)
        return HttpResponseBadRequest('Invalid request')
            