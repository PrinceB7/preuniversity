from django.conf.urls import url
from django.contrib.auth import views as dj_views
from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^$', views.dashboard, name='dashboard'),

    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),

    # login / logout urls
    url(r'^login/$', dj_views.login, name='login'),
    url(r'^logout/$', dj_views.logout, name='logout'),
    url(r'^logout-then-login/$', dj_views.logout_then_login, name='logout_then_login'),

    # change password urls
    url(r'^password-change/$', dj_views.password_change, name='password_change'),
    url(r'^password-change/done/$', dj_views.password_change_done, name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$', dj_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', dj_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', dj_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', dj_views.password_reset_complete, name='password_reset_complete'),
]
