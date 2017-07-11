from django.shortcuts import render, HttpResponseRedirect
from .models import Follower
import datetime
from django.contrib.auth import get_user_model
import logging
logger = logging.getLogger(__name__)


def main_view(request, pages_user=None):
    user = request.user
    if not user.is_authenticated and pages_user is None:
        # Todo make sign up or view trends page
        pass
    if user.is_authenticated and pages_user is None:
        return HttpResponseRedirect('/%s/' % user.username)

    on_self_page = False
    if user.username == pages_user:
        on_self_page = True
    UserModel = get_user_model()
    pages_user = UserModel.objects.get(username=pages_user)
    posts = pages_user.post_set.order_by('-time_posted')
    followed = bool(Follower.objects.filter(idol=pages_user, user=user))
    followers = len(Follower.objects.filter(idol=pages_user))
    following = len(Follower.objects.filter(user=pages_user))
    return render(request, 'main/main.html', {'user': user,
                                              'pages_user': pages_user,
                                              'posts': posts,
                                              'on_self_page': on_self_page,
                                              'followers': followers,
                                              'following': following,
                                              'followed': followed,
                                              'time_now': datetime.datetime.now()
                                              })
