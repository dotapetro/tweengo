from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_by', default='')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_by', default='')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE, default='')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s` profile' % self.user.username


class TestPost(models.Model):
    author = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    body = models.TextField(max_length=500)
    time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s`s TEST post' % self.username
