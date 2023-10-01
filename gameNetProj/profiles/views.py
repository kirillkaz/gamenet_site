from django.conf import settings
from django.contrib.auth import login, authenticate

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse, HttpResponseBadRequest

from .serializers import UserImagesSerializer
from .models import User, UserImages, Bio, User_Friends
from .forms import CustomRegisterForm, CustomAuthForm, ProfileSettingsForm
from activityApp.models import UserPosts, UserPostComment

from tools.load_avatar import LoadUserAvatar, LoadUserCover
from tools.links import SETTINGS_LINK, PROFILE_LINK
from tools.ajax_wrapper import get_ajax_wrapper


@csrf_exempt
def register_auth(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm()
        auth_form = CustomAuthForm(request.POST)

        if 'email' in request.POST:
            register_form = CustomRegisterForm(request.POST)
            if register_form.is_valid():
                #user creation
                user = register_form.save()
                user.refresh_from_db()
                user.save()

                #bio creation
                user_bio = Bio.objects.create(user_id=user)
                user_bio.save()

                #friend list creation
                user_friends = User_Friends.objects.create(user_id=user)
                user_friends.save()

                login(request, user)
                return redirect(reverse('activityApp:news_page'))
        
        elif auth_form.is_valid():
            user = authenticate(login=auth_form.cleaned_data['login'], password=auth_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('activityApp:news_page'))

        else:
            register_form = CustomRegisterForm()
            auth_form = CustomAuthForm()
        
    else:
        register_form = CustomRegisterForm()
        auth_form = CustomAuthForm()

    context = {
        'register_form': register_form,
        'auth_form': auth_form,
    }
    return render(request, 'auth_register/register_auth.html', context=context)


def profiles_page(request, username):
    profile_owner_avatar = LoadUserAvatar(username)
    user_avatar = LoadUserAvatar(request.user.login)
    cleaned_cover = LoadUserCover(username)
    try:
        user = User.objects.get(login=username)
    except:
        pass
    context = {
        'profile_owner_avatar': profile_owner_avatar,
        'user_avatar': user_avatar,
        'user_cover': cleaned_cover,
        'profile_owner': user,
        }
    return render(request, 'profiles/profiles.html', context=context)


def profile_menu_ajax(request):
    try:
        profile_link = PROFILE_LINK + request.user.login
    except:
        profile_link = ''
        error = 'Внимание, вы не авторизованый пользователь!'

    #TODO сделать всплывающее окно для ошибки!

    context = {
                'profile_link': profile_link,
                'settings_link': SETTINGS_LINK,
            }
    url = 'ajax/profiles_ajax.html'
    
    return get_ajax_wrapper(request=request, url=url, context=context)


def user_posts_ajax(request, username):
    user_avatar = LoadUserAvatar(username)
    user_posts = UserPosts.objects.filter(creator_id=username)

    context = {
        'user_posts': user_posts,
        'user_avatar': user_avatar,
    }

    url = 'ajax/posts_ajax.html'    

    return get_ajax_wrapper(request=request, url=url, context=context)


def user_show_comments_ajax(request, post_id):
    class PostContent:
        def __init__(self, text, avatar):
            self.text = text
            self.avatar = avatar

    raw_comments = UserPostComment.objects.filter(post_id=post_id)
    
    comments = []
    for comment in raw_comments:
        avatar = LoadUserAvatar(comment.user_id)
        post = PostContent(comment.text, avatar)
        comments.append(post)
    
    context = {
        'comments': comments,
    }

    url = 'ajax/comments_ajax.html'

    return get_ajax_wrapper(request, url, context)
    


def settings_page(request):
    username = request.user.login
    user_avatar = LoadUserAvatar(username)

    context = {
        'user_avatar': user_avatar,
    }

    return render(request, 'profiles/settings.html', context)


def profile_settings_ajax(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            user = request.user
            user_avatar = LoadUserAvatar(user.login)
            user_cover = LoadUserCover(user.login)
            user_bio = Bio.objects.get(user_id=user.login)

            form = ProfileSettingsForm(initial={
                'name': user.name,
                'surname': user.surname,
                'status': user_bio.user_description,
                'sex': user_bio.sex,
                'phone': user.phone,
                'birthday': user_bio.birthday,
            })

            context = {
                'user_avatar': user_avatar,
                'user_cover': user_cover,
                'form': form,
            }
            return render(request, 'ajax/profile_settings_ajax.html', context)
        
        elif request.method == 'POST':
            form = ProfileSettingsForm(request.POST, request.FILES)

            if form.is_valid():
                try:
                    username = request.user.login
                    user = User.objects.get(login=username)
                    user_bio = Bio.objects.get(user_id=username)

                    if form.cleaned_data.get('name'):
                        user.name = form.cleaned_data.get('name')

                    if form.cleaned_data.get('surname'):
                        user.surname = form.cleaned_data.get('surname')

                    if form.cleaned_data.get('status'):
                        user_bio.user_description = form.cleaned_data.get('status')

                    if form.cleaned_data.get('sex'):
                        user_bio.sex = form.cleaned_data.get('sex')[0].upper()

                    if form.cleaned_data.get('phone'):
                        user.phone = form.cleaned_data.get('phone')

                    if form.cleaned_data.get('avatar'):
                        user_avatar = UserImages.objects.create(
                            user_id=user,
                            image=form.cleaned_data.get('avatar'))
                        user_avatar.save()

                        user.avatar_id = user_avatar.id

                        user.galary.add(user_avatar)

                    if form.cleaned_data.get('cover'):
                        user.cover = form.cleaned_data.get('cover')

                    user.save()
                    user_bio.save()

                    return HttpResponse(f'<h1>Успех!</h1>')

                except:
                    error = 'Ошибка обработки формы!'
                    return HttpResponse(f'<h1>{error}</h1>')

        else:
            return JsonResponse({'req_error': 'invalid request'}, status=400)
        
    else:
        return HttpResponseBadRequest('Invalid request')

