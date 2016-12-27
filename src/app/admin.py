from django.contrib import admin
from .models import News, Testimonial


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']


admin.site.register(News, NewsAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
