from django.conf.urls import url
from . import views
from django.contrib.auth.views import *
from django.urls import path, re_path
from django_filters.views import FilterView
from .filters import UserFilter
from .models import Profile


app_name = 'participante'
handler404 = 'views.not_found_page_view'

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    path('', views.homepage, name='homepage'),
    path('dash/', views.dashboard, name='dashboard'),
    #path('lojista/', views.lojista, name='notfound'),
    # path('search/', FilterView.as_view(filterset_class=UserFilter,
    #     template_name='participante/participante_list.html'), name='search'),
    path('search/', views.search, name='search'),
    path('participante/cpf', views.search_by_cpf, name='search_by_cpf'),

    url(r'^list$', views.participante_list, name='list'),


    re_path(r'^participante/(?P<username>[-\w]+)/detail$', views.user_detail, name='user_detail'),
    re_path(r'^participante/edit/(?P<username>[-\w]+)/$', views.user_edit, name='user_edit'),
    # Coupons paths
    path('docsfiscais/', views.doclist, name='docsfiscais'),

    # Coupons paths
    path('coupons/', views.coupons, name='coupons'),

    # Premios paths
    path('premios/', views.premios, name='premios'),


    path('cadastrar/', views.register, name='register'),
    path('register/', views.register2, name='register-op'),
    path('edit/', views.edit, name='edit'),

    # Documentos Fiscais paths
    path('adddocfiscal/', views.adddocfiscal, name='adddocfiscal'),
    re_path(r'^adddocfiscal/(?P<username>[-\w]+)/$', views.adddocfiscalbyop, name='adddocfiscalbyop'),
    path('editdocfiscal/', views.editdocfiscal, name='editdocfiscal'),
    re_path(r'^editdocfiscal/(?P<numerodocumento>[\d,.?!]+)/$', views.editdocfiscal, name='editdocfiscal'),

    # login / logout paths
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),

    # change password paths
    path('password-change/',password_change, name='password_change'),
    path('password-change/done/', password_change_done, name='password_change_done'),

    # restore password paths
    path('password-reset/', password_reset, name='password_reset'),
    path('password-reset/done/', password_reset_done, name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', password_reset_complete, name='password_reset_complete'),


]
