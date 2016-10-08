# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20161008_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(choices=[('tashkent_city', 'Toshkent shahri'), ('tashkent_region', 'Toshkent viloyati'), ('andijan', 'Andijon'), ('fergana', "Farg'ona"), ('namangan', 'Namangan'), ('sirdarya', 'Sirdaryo'), ('jizzax', 'Jizzax'), ('samarqand', 'Samarqand'), ('qashqadaryo', 'Qashqadaryo'), ('surhandaryo', 'Surhandaryo'), ('buxoro', 'Buxoro'), ('navoiy', 'Navoiy'), ('xorazm', 'Xorazm'), ('qoraqalpogiston', "Qoraqalpog'iston")], default='tashkent_city', max_length=50),
        ),
    ]