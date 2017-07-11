# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20170710_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
