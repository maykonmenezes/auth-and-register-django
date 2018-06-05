"""liquida2018 URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', include('participante.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^participante/', include('participante.urls')),
    # python-social-auth
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
