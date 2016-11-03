from django.contrib import admin
from django.template.defaultfilters import safe
from .models import *


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_description', 'created_date']
    fields = ['name', 'description']

    def get_description(self, obj):
        return safe(obj.description[:100])


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_description', 'image', 'subject']
    fields = ['subject', 'title', 'description', 'image', 'video', 'position']

    def get_description(self, obj):
        return safe(obj.description[:100])


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topics, TopicAdmin)
