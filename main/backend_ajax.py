import logging
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Post, Like, Follower
from .forms import PostImageForm
logger = logging.getLogger(__name__)


def login_user(request):
    if request.method == 'POST':
        if request.POST['action'] != 'login_user':
            data = {
                'user_signed_in': False,
                'error': 'Don`t play with js ;)'
            }
            return JsonResponse(data)
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=request.POST['username'])
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=request.POST['username'])
            except UserModel.DoesNotExist:
                data = {
                    'user_signed_in': False,
                    'error': 'There is no user with that username or email'
                }
                return JsonResponse(data)
        user = authenticate(username=user.username, password=request.POST['password'])
        if user is None:
            data = {
                'user_signed_in': False,
                'error': 'Password is incorrect'
            }
            return JsonResponse(data)
        else:
            login(request=request, user=user)
            data = {
                'user_signed_in': True
            }
            return JsonResponse(data)


def tweet(request):
    if request.method == 'POST':
        Post.objects.create(user=request.user, body=request.POST['body']).save()
        data = {
            'tweeted': True
        }
        return JsonResponse(data)


def add_image_to_tweet(request):
    if request.method == 'POST':
        form = PostImageForm(files=request.FILES)
        if not form.is_valid():
            data = {
                'image_added': False,
                'error': 'wat da fuck??'
            }
            return JsonResponse(data)
        a = request.user.post_set.order_by('-id')[0]
        a.image = form.cleaned_data['image']
        a.save()
        logger.error(a.image.url)
        data = {
            'image_added': True,
            'image_link': a.image.url
        }
        return JsonResponse(data)


def like_unlike(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        try:
            like = post.like_set.get(user_id=request.user.id)
            like.delete()
        except ObjectDoesNotExist:
            Like.objects.create(user=request.user, post=post)
        data = {
            'liked': True,
        }
        return JsonResponse(data)


def follow_un_follow(request):
    if request.method == 'POST':
        UserModel = get_user_model()
        idol = UserModel.objects.get(id=request.POST['idol_id'])
        try:
            follower = Follower.objects.get(user=request.user, idol=idol)
            follower.delete()
        except ObjectDoesNotExist:
            Follower.objects.create(user=request.user, idol=idol)
        data = {
            'followed': True,
        }
        return JsonResponse(data)


def get_post_batch(number):
    return [number*20 - 20, number * 20 - 1]


def load_more_posts(request):
    if request.method == 'POST':
        UserModel = get_user_model()
        pages_user = UserModel.objects.get(id=request.POST['pages_user_id'])
        batch_range = get_post_batch(int(request.POST['batch']))
        if batch_range[1] > pages_user.post_set.count:
            if batch_range[0] > pages_user.post_set.count:
                data = {
                    'post_loaded': False,
                    'posts_ended': True
                }
                return JsonResponse(data)
            batch_range[1] = pages_user.post_set.count - 1
        posts = pages_user.post_set.order_by('-time_posted')[batch_range[0]: batch_range[1]]
        data = {
            'post_loaded': True,
            'posts': [{'body': post.body, 'time_posted': post.time_posted, 'image_url': post.image.url} for post in posts]
        }
        return JsonResponse(data)


