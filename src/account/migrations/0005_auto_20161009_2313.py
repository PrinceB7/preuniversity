# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 18:13
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20161008_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='profile',
            name='self_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
