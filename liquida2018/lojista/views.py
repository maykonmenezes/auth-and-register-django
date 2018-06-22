from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LojistaRegistrationForm, RamoAtividadeRegistrationForm
from .models import Lojista, RamoAtividade
from django.contrib.auth.decorators import user_passes_test
from .filters import LojistaFilter
from django.db.models.functions import Lower, Upper

@login_required
@user_passes_test(lambda u: u.is_superuser)
def search(request):
      lojista_list = Lojista.objects.all().order_by(Upper('fantasiaLojista').asc())
      lojista_filter = LojistaFilter(request.GET, queryset=lojista_list)
      return render(request, 'lojista/lojistas_list.html', {'filter': lojista_filter,
                                                                     'section':'lojistas'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def homepage(request):
    return render(request, 'lojista/dashboard.html', {'section': 'lojista'})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def register(request):
    if request.method == 'POST':
        lojista_form = LojistaRegistrationForm(request.POST)
        ramoatividade_form = RamoAtividadeRegistrationForm(request.POST)
        if lojista_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_lojista = lojista_form.save(commit=False)
            # Save the User object
            new_lojista.save()
            return render(request,
                          'lojista/register_done.html',
                          {'new_lojista': new_lojista})
        elif ramoatividade_form.is_valid():
            new_ramoatividade = ramoatividade_form.save()
            messages.success(request, 'Ramo adicionado com sucesso')
        else:
            messages.error(request, 'Erro ao adicionar novo ramo!')

    else:
        lojista_form = LojistaRegistrationForm()
        ramoatividade_form = RamoAtividadeRegistrationForm()
    return render(request, 'lojista/register.html', {'lojista_form': lojista_form, 'ramoatividade_form':ramoatividade_form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil atualizado com sucesso')
        else:
            messages.error(request, 'Erro na atualização do perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'participante/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})

@login_required
def editlojista(request, ielojista):
    if request.method == 'POST':
        instance = get_object_or_404(Lojista, IELojista=ielojista)
        lojista_form = LojistaRegistrationForm(instance=instance)
        if lojista_form.is_valid():
            lojista_form.save()
            messages.success(request, 'Perfil atualizado com sucesso')
        else:
            messages.error(request, 'Erro na atualização do Lojista')
    else:
        instance = get_object_or_404(Lojista, IELojista=ielojista)
        lojista_form = LojistaRegistrationForm(instance=instance)
    return render(request, 'lojista/edit.html', {'lojista_form': lojista_form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def lojistalist(request):
    lojistas = Lojista.objects.all()
    return render(request, 'lojista/list_lojistas.html', {'section': 'listar-lojistas',
                                                      'lojistas': lojistas})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def registeratividade(request):
    if request.method == 'POST':
        ramoatividade_form = RamoAtividadeRegistrationForm(request.POST)

        if ramoatividade_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_ramoatividade = ramoatividade_form.save(commit=False)
            # Save the User object
            new_ramoatividade.save()
            return render(request,
                          'lojista/register_ramo_atividade_done.html',
                          {'new_ramoatividade': new_ramoatividade})
    else:
        ramoatividade_form = RamoAtividadeRegistrationForm()
    return render(request, 'lojista/register_ramo_atividade.html', {'ramoatividade_form': ramoatividade_form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def listatividade(request):
    ramosatividade = RamoAtividade.objects.all()
    return render(request, 'lojista/list_ramo_atividade.html', {'section': 'ramoatividade',
                                                      'ramosatividade': ramosatividade})
