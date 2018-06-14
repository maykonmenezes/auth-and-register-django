from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'lojista'

urlpatterns = [
    # Lojistas urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('list/', views.lojistalist, name='list'),

    # Ramo de atividades pathpatterns
    path('registeratividade/', views.registeratividade, name='registeratividade'),
    path('listatividade/', views.listatividade, name='listatividade'),
]
