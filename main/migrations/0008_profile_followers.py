# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_testpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Profile'),
            preserve_default=False,
        ),
    ]
