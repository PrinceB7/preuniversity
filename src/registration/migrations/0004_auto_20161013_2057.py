# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 15:57
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_migrate_activatedstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 10, 13, 15, 57, 4, 711564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='registrationprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]