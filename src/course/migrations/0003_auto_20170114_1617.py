# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-14 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20170114_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.CharField(choices=[('mathematics', 'Mathematics'), ('physics', 'Physics'), ('english', 'English'), ('IELTS', 'IELTS')], default='mathematics', max_length=15),
        ),
        migrations.AlterField(
            model_name='homework',
            name='subject',
            field=models.CharField(choices=[('mathematics', 'Mathematics'), ('physics', 'Physics'), ('english', 'English'), ('IELTS', 'IELTS')], default='mathematics', max_length=15),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(choices=[('mathematics', 'Mathematics'), ('physics', 'Physics'), ('english', 'English'), ('IELTS', 'IELTS')], default='mathematics', max_length=15),
        ),
    ]
