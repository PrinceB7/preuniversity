from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=254)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
