from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
# from account import urls
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^account/', include(urls)),
    url(r'^accounts/', include('registration.urls')),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
