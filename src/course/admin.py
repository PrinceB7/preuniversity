from django.contrib import admin
from django.template.defaultfilters import safe
from .models import Subject, File, Topic, Homework, Exam


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_description', 'created_date', 'last_modified_date']
    fields = ['name', 'description']

    def get_description(self, obj):
        return safe(obj.description[:30])


class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']


class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_description', 'image', 'subject', 'created_date', 'last_modified_date']
    fields = ['subject', 'title', 'description', 'image', 'video', 'position', 'files']

    def get_description(self, obj):
        return safe(obj.description[:30])


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject']


class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'subject']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(File, FileAdmin)
