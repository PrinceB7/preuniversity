from django.db import models
from ckeditor.fields import RichTextField


class Subject(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='lectures/')
    subject = models.ForeignKey(Subject, related_name='lectures')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Topics(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='topics/')
    lecture = models.ForeignKey(Lecture, related_name='topics')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=511, blank=True)
    description = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='contents/images/')
    video = models.FileField(blank=True, upload_to='contents/videos/')
    topic = models.ForeignKey(Topics, related_name='contents')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

