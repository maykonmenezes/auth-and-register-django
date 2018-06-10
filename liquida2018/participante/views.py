from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, UserAddFiscalDocForm
from .models import Profile, DocumentoFiscal

def homepage(request):
    return render(request, 'participante/index.html', {'section': 'homepage'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Autenticado com sucesso!')
                else:
                    return HttpResponse('Conta desativada!')
            else:
                return HttpResponse('Login inválido!')
    else:
        form = LoginForm()
    return render(request, 'participante/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)
            return render(request,
                          'participante/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'participante/register.html', {'user_form': user_form})


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
def adddocfiscal(request):
    if request.method == 'POST':
        documentoFiscal_form = UserAddFiscalDocForm(request.POST)
        user = request.user
        if documentoFiscal_form.is_valid():
            # Create a new document object but avoid saving it yet
            new_documentoFiscal = documentoFiscal_form.save(commit=False)
            # Set the user
            new_documentoFiscal.user = user
            # Save the doc object
            new_documentoFiscal.save()
            return render(request,
                          'participante/doc_fiscal_done.html',
                          {'new_documentoFiscal': new_documentoFiscal})
    else:
        documentoFiscal_form = UserAddFiscalDocForm()
    return render(request, 'participante/doc_fiscal_add.html', {'documentoFiscal_form': documentoFiscal_form})

@login_required
def doclist(request):
    docs = DocumentoFiscal.objects.filter(user=request.user)
    return render(request, 'participante/list_doc_fiscal.html', {'section': 'docsfiscais',
                                                      'docs': docs})

@login_required
def editdocfiscal(request):
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
def dashboard(request):
    return render(request, 'participante/dashboard.html', {'section': 'dashboard'})

@login_required
def coupons(request):
    return render(request, 'participante/coupons.html', {'section': 'coupons'})

@login_required
def premios(request):
    return render(request, 'participante/premios.html', {'section': 'premios'})

@login_required
def lojista(request):
    return render(request, 'lojista/dashboard.html', {'section': 'lojista'})
