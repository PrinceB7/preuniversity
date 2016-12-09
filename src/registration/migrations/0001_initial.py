# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 11:17
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('activated', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.date.today)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('date_of_join', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('region', models.CharField(choices=[('tashkent_city', 'Toshkent shahri'), ('tashkent_region', 'Toshkent viloyati'), ('andijan', 'Andijon'), ('fergana', "Farg'ona"), ('namangan', 'Namangan'), ('sirdarya', 'Sirdaryo'), ('jizzax', 'Jizzax'), ('samarqand', 'Samarqand'), ('qashqadaryo', 'Qashqadaryo'), ('surhandaryo', 'Surhandaryo'), ('buxoro', 'Buxoro'), ('navoiy', 'Navoiy'), ('xorazm', 'Xorazm'), ('qoraqalpogiston', "Qoraqalpog'iston")], default='tashkent_city', max_length=50)),
                ('self_description', ckeditor.fields.RichTextField(blank=True)),
                ('mathematics_access', models.PositiveIntegerField(default=0)),
                ('physics_access', models.PositiveIntegerField(default=0)),
                ('english_access', models.PositiveIntegerField(default=0)),
                ('ielts_access', models.PositiveIntegerField(default=0)),
                ('is_teacher', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
