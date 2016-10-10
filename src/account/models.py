from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Profile(models.Model):
    REGIONS = (
        ('tashkent_city', 'Toshkent shahri'),
        ('tashkent_region', 'Toshkent viloyati'),
        ('andijan', 'Andijon'),
        ('fergana', 'Farg\'ona'),
        ('namangan', 'Namangan'),
        ('sirdarya', 'Sirdaryo'),
        ('jizzax', 'Jizzax'),
        ('samarqand', 'Samarqand'),
        ('qashqadaryo', 'Qashqadaryo'),
        ('surhandaryo', 'Surhandaryo'),
        ('buxoro', 'Buxoro'),
        ('navoiy', 'Navoiy'),
        ('xorazm', 'Xorazm'),
        ('qoraqalpogiston', 'Qoraqalpog\'iston'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    date_of_join = models.DateTimeField(blank=True, default=now)
    region = models.CharField(max_length=50, choices=REGIONS, default='tashkent_city')
    self_description = RichTextField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
