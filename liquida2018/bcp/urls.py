"""
Module: Barcode Printer URLS
Project: Django BCP
Copyright: Adlibre Pty Ltd 2012
License: See LICENSE for license information
"""

from django.conf.urls import url
from . import views
from django.contrib.auth.views import *
from django.urls import path, re_path
#import mdtui.views

app_name = 'bcp'

urlpatterns = [
    re_path(r'^(?P<numerodocumento>[-\w]+)/(?P<code>[\w-]+)$', views.generate, name='generate'),
    re_path(r'^(?P<barcode_type>(Standard39|Code128))/(?P<code>[\w-]+)/print$', views.print_barcode, name='print'),
    re_path(r'^(?P<numerodocumento>[-\w]+)/(?P<code>[\w-]+)/print_qrcode$', views.print_qrcode, name='print_qrcode'),
    re_path(r'^(?P<barcode_type>(Standard39|Code128))/(?P<code>[\w-]+)/test', views.print_barcode_embed_example, name='embed-example'),
]
