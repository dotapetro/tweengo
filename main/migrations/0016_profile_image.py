# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170709_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]