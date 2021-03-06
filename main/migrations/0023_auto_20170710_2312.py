# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 20:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0022_auto_20170710_2305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='shared',
        ),
        migrations.AddField(
            model_name='post',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='shared_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='shared_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
