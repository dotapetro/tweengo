from django.shortcuts import render
from .models import TestPost
import datetime

def main_view(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = False
    posts = TestPost.objects.order_by('-time_posted')
    return render(request, 'main/main.html', {'user': user,
                                              'pages_user': user,
                                              'posts': posts,
                                              'time_now': datetime.datetime.now()
                                              })
