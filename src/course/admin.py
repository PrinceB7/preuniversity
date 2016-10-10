from django.contrib import admin
from django.template.defaultfilters import safe
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_description', 'created_date']
    fields = ['name', 'description']

    def get_description(self, obj):
        return safe(obj.description[:100])


class LectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_description', 'image', 'subject']
    fields = ['title', 'description', 'image', 'subject']

    def get_description(self, obj):
        return safe(obj.description[:100])


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_description', 'image', 'lecture']
    fields = ['title', 'description', 'image', 'lecture']

    def get_description(self, obj):
        return safe(obj.description[:100])


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_description', 'image', 'video', 'topic']
    fields = ['title', 'description', 'image', 'video', 'topic']

    def get_description(self, obj):
        return safe(obj.description[:100])

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Topics, TopicAdmin)
admin.site.register(Content, ContentAdmin)
