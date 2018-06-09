from django.conf.urls import url
from . import views

urlpatterns = [
    # Lojistas urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
]
