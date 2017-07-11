from django.db import models
from django.contrib.auth.models import User
import datetime


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner', null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    body = models.TextField(max_length=500, default='')
    time_posted = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,  null=True, blank=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', null=True, blank=True)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', null=True, blank=True)
    image = models.ImageField(default='')
    comments_allowed = models.BooleanField(default=False)
    show_page_for_anonymous_user = models.BooleanField(default=True)

    def __str__(self):
        return '%s`s profile' % self.user.username

    def as_dict(self):
        return {
            'user_username': self.user.username,
            'followers': self.followers,
            'following': self.following,
        }


class Follower(models.Model):
    # That is follower
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_user')
    # That is what he following
    idol = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_idol')


class TestPost(models.Model):
    author = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    body = models.TextField(max_length=500)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s`s TEST post' % self.username
