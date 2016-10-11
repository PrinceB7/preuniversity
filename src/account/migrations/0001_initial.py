# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 06:01
from __future__ import unicode_literals

import ckeditor.fields
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('date_of_join', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('region', models.CharField(choices=[('tashkent_city', 'Toshkent shahri'), ('tashkent_region', 'Toshkent viloyati'), ('andijan', 'Andijon'), ('fergana', "Farg'ona"), ('namangan', 'Namangan'), ('sirdarya', 'Sirdaryo'), ('jizzax', 'Jizzax'), ('samarqand', 'Samarqand'), ('qashqadaryo', 'Qashqadaryo'), ('surhandaryo', 'Surhandaryo'), ('buxoro', 'Buxoro'), ('navoiy', 'Navoiy'), ('xorazm', 'Xorazm'), ('qoraqalpogiston', "Qoraqalpog'iston")], default='tashkent_city', max_length=50)),
                ('self_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
