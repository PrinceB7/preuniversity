from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^poll/', include(poll_urls)),
    # url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^admin/', admin.site.urls),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
]

urlpatterns += i18n_patterns(
                             url(r'^accounts/', include('registration.urls')),
                             url(r'^q/', include('Exam.quiz.urls')),
                             url(r'^course/', include('course.urls')),
                             )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
