from django.db import models
from ckeditor.fields import RichTextField


class Subject(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Topics(models.Model):
    title = models.CharField(max_length=255, blank=True)
    video = models.FileField(blank=True, upload_to='topics/video/')
    description = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='topics/image/')
    subject = models.ForeignKey(Subject, related_name='topics')

    position = models.PositiveIntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.subject_name = self.subject.name
        super(Topics, self).save(*args, **kwargs)

    def get_next(self):
        nextt = Topics.objects.filter(position__gt=self.position)
        if nextt:
            return nextt.first()

    def get_previous(self):
        previous = Topics.objects.filter(position__lt=self.position)
        if previous:
            return previous.last()


