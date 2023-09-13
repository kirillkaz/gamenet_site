from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import GroupPosts, UserPosts
from .forms import PostForm
from groups.models import Group
from profiles.models import User, User_Friends

from tools.links import GROUP_LINK

from tools.load_avatar import LoadUserAvatar

class PostsAPIView(APIView):
    def get(self, request, user_login):
        # user_login = request.GET["login"]
        # user = User.objects.get(login=user_login)
        
        #get groups posts
        group_ids = Group.objects.filter(subscribers__login=user_login).values_list('id')
        g_posts = []

        for id in group_ids:
            group_posts = GroupPosts.objects.filter(creator_id=id).values()
            g_posts.extend(group_posts)

        #get user's friends posts
        user_friends_ids = User_Friends.objects.filter(friends__login=user_login).values_list('user_id_id')

        fr_posts = []
        for login in user_friends_ids:
            friend_posts = UserPosts.objects.filter(creator_id=login).values()
            fr_posts.extend(friend_posts)


        #create and sort posts arr
        posts = g_posts[:]
        posts.extend(fr_posts[:])
        posts = sorted(posts, key=lambda post: post['date'])
        return Response({'posts': list(posts)})
    

def news_page_view(request):
    username = request.user.login
    user_avatar = LoadUserAvatar(username)

    context = {'groups_link': GROUP_LINK, 'user_avatar': user_avatar}
    return render(request, 'news_page.html', context)


def post_form_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            form = PostForm()
            context = {
                'form': form,
            }
            return render(request, 'activityApp/ajax/postform_ajax.html', context)
        
        elif request.method == 'POST':
            form = PostForm(request.POST)

            if form.is_valid():
                user_post = UserPosts.objects.create(creator_id=request.user, text=form.cleaned_data.get('textfield'))
                return HttpResponse('<h1>Успех!</h1>')
            
            else:
                return JsonResponse({'form_error': form.errors}, status=400)
        else:
            return JsonResponse({'req_error': 'invalid request'}, status=400)
        
    else:
        return HttpResponseBadRequest('Invalid request')

