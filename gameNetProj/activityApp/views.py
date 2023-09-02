from django.shortcuts import render
from .models import GroupPosts, UserPosts
from rest_framework.views import APIView
from rest_framework.response import Response
from groups.models import Group
from profiles.models import User, User_Friends
from .links import GROUP_LINK

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
    context = {'groups_link': GROUP_LINK}
    return render(request, 'news_page.html', context)

