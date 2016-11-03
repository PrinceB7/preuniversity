from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^subject/(?P<name>\w+)/$', views.detail_of_subject, name='detail_of_subject'),
    url(r'^subject/topic/(?P<topic_title>\w+)', views.detail_of_topic, name='detail_of_topic'),

]
