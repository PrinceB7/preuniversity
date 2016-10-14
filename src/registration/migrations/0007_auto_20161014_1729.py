# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 12:29
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20161014_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registrationprofile',
            options={'verbose_name': 'profile', 'verbose_name_plural': 'profiles'},
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='date_of_join',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='region',
            field=models.CharField(choices=[('tashkent_city', 'Toshkent shahri'), ('tashkent_region', 'Toshkent viloyati'), ('andijan', 'Andijon'), ('fergana', "Farg'ona"), ('namangan', 'Namangan'), ('sirdarya', 'Sirdaryo'), ('jizzax', 'Jizzax'), ('samarqand', 'Samarqand'), ('qashqadaryo', 'Qashqadaryo'), ('surhandaryo', 'Surhandaryo'), ('buxoro', 'Buxoro'), ('navoiy', 'Navoiy'), ('xorazm', 'Xorazm'), ('qoraqalpogiston', "Qoraqalpog'iston")], default='tashkent_city', max_length=50),
        ),
        migrations.AddField(
            model_name='registrationprofile',
            name='self_description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]