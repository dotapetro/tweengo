from django.contrib import admin
from .models import Post, Profile, Comment, TestPost, Like


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(TestPost)
admin.site.register(Like)
