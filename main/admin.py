from django.contrib import admin
from .models import Post, Profile, Comment, TestPost


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(TestPost)

