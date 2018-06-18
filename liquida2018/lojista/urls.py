from django.conf.urls import url
from django.urls import path
from . import views
from django_filters.views import FilterView
from .filters import LojistaFilter

app_name = 'lojista'

urlpatterns = [
    # Lojistas urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('list/', views.lojistalist, name='list'),

    # path('search/', FilterView.as_view(filterset_class=LojistaFilter,
    #     template_name='lojista/lojistas_list.html'), name='search'),
    path('search/', views.search, name='search'),
    # Ramo de atividades pathpatterns
    path('registeratividade/', views.registeratividade, name='registeratividade'),
    path('listatividade/', views.listatividade, name='listatividade'),
]
