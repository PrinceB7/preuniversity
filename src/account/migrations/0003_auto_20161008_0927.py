# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_of_join',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='region',
            field=models.CharField(default='tashkent_city', max_length=50),
        ),
    ]