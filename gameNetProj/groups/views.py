from io import BytesIO
import requests

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


def get_groups_api():
    url = f'http://37.139.33.69/api/v1/groups/kirill'
    req = requests.get(url)
    return req.text


def groups_page_view(request):
    #try:
    data = get_groups_api()
    #cleaned_data = JSONParser.parse(BytesIO(data))
    #obj_avatar = cleaned_data['0']['avatar']
    obj_avatar = ''
    #except:
     #   obj = ''
    context  = {'obj_avatar': obj_avatar}
    return render(request, 'groups_page.html', context)
