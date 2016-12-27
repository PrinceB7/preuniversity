from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=254)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'


class Testimonial(models.Model):
    name = models.CharField(max_length=127)
    text = RichTextField()
    photo = models.ImageField(upload_to='testimonials/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
