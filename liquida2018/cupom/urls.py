from django.conf.urls import url
from . import views
from django.urls import path, re_path


app_name = 'cupom'

urlpatterns = [
    # cupom urlpatterns = [
    #path('', views.addcupom, name='detail'),
    re_path(r'^generate/(?P<numerodocumento>[-\w]+)/$', views.addcupom, name='detail'),
    re_path(r'^cupons/(?P<username>[-\w]+)/$', views.cupomlist, name='list'),

]
