from datetime import timedelta
from django.db import models
from django.template.defaultfilters import safe
from ckeditor.fields import RichTextField
from social.utils import slugify

SUBJECTS = (
    ('mathematics', 'Mathematics'),
    ('physics', 'Physics'),
    ('english', 'English'),
    ('ielts', 'IELTS'),
)


class Topic(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)
    video = models.FileField(blank=True, upload_to='topics/video/')
    description = RichTextField(blank=True)
    image = models.ImageField(blank=True, upload_to='topics/image/')
    subject = models.CharField(max_length=15, choices=SUBJECTS, default=SUBJECTS[0][1])
    files = models.ManyToManyField('File', related_name='topic_files')

    level = models.PositiveIntegerField(default=0)

    position = models.PositiveIntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def get_next(self):
        nextt = Topic.objects.filter(position__gt=self.position, subject__exact=self.subject)
        if nextt:
            return nextt.first()

    def get_previous(self):
        previous = Topic.objects.filter(position__lt=self.position, subject__exact=self.subject)
        if previous:
            return previous.last()


class Homework(models.Model):
    subject = models.CharField(max_length=15, choices=SUBJECTS, default=SUBJECTS[0][1])
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)
    description = RichTextField(blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()

    file = models.ManyToManyField('File', related_name='homework_files')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Homework, self).save(*args, **kwargs)


class Exam(models.Model):

    EXAM_STATUS = (
        ('coming', 'Coming'),
        ('going', 'Going'),
        ('ended', 'Ended'),
    )

    subject = models.CharField(max_length=15, choices=SUBJECTS, default=SUBJECTS[0][0])
    level = models.PositiveIntegerField(default=1, blank=True)
    date = models.DateTimeField()
    duration = models.DurationField(blank=True, default=timedelta(minutes=90))
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(blank=True)
    description = RichTextField(blank=True)
    files = models.ManyToManyField('File', related_name='exam_files')
    status = models.CharField(max_length=50, blank=True, choices=EXAM_STATUS, default=EXAM_STATUS[0][1])

    def __str__(self):
        return 'lvl:' + str(self.level) + ' ' + self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Exam, self).save(*args, **kwargs)


class File(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    file = models.FileField(upload_to='allfiles/')

    def __str__(self):
        return self.name + ' ' + safe(self.description[:20])
