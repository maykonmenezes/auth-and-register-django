from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LojistaRegistrationForm, RamoAtividadeRegistrationForm
from .models import Lojista, RamoAtividade

def homepage(request):
    return render(request, 'lojista/dashboard.html', {'section': 'homepage'})

@login_required
def register(request):
    if request.method == 'POST':
        lojista_form = LojistaRegistrationForm(request.POST)

        if lojista_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_lojista = lojista_form.save(commit=False)
            # Save the User object
            new_lojista.save()
            return render(request,
                          'lojista/register_done.html',
                          {'new_lojista': new_lojista})
    else:
        lojista_form = LojistaRegistrationForm()
    return render(request, 'lojista/register.html', {'lojista_form': lojista_form})

@login_required
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
def lojistalist(request):
    lojistas = Lojista.objects.all()
    return render(request, 'lojista/list_lojistas.html', {'section': 'lojistas',
                                                      'lojistas': lojistas})


@login_required
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
def listatividade(request):
    ramosatividade = RamoAtividade.objects.all()
    return render(request, 'lojista/list_ramo_atividade.html', {'section': 'ramoatividade',
                                                      'ramosatividade': ramosatividade})
