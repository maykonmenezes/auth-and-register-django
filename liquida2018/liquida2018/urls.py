"""liquida2018 URL Configuration
"""
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from participante import urls as purls
from lojista import urls as lurls
from cupom import urls as curls
from bcp import urls as burls

handler404 = 'participante.views.not_found_page_view'

urlpatterns = [
    path('', include(purls)),
    path('nimda/', admin.site.urls),
    url('cupom/', include(curls, namespace='cupom')),
    path('lojista/', include(lurls, namespace='lojista')),
    path('barcode/', include(burls, namespace='bcp')),
    # python-social-auth
    #url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
