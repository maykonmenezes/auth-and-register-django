from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import Profile, DocumentoFiscal
from lojista.models import Lojista
from .filters import UserFilter, DocFilter
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models.functions import Lower, Upper
from cupom.forms import AddCupomForm
from cupom.models import Cupom

def not_found_page_view(request):
    return render(request, 'not_found.html')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def search(request):
      user_list = Profile.objects.all().order_by(Upper('nome').asc())
      user_filter = UserFilter(request.GET, queryset=user_list)
      return render(request, 'participante/participante_list.html', {'filter': user_filter,
                                                                     'section':'participantes'})

def search_by_cpf(request):
    if(request.GET.get('q')):
        if 'q' in request.GET is not None:
            cpf = request.GET.get('q')
            profile = get_object_or_404(Profile, CPF=cpf)
            user = get_object_or_404(User, username= profile.user.username)
            docs = DocumentoFiscal.objects.filter(user=user)
            return render(request, 'participante/detail.html', {'section': 'people','user': profile, 'docs': docs})
        else:
            messages.error(request, 'CPF não encontrado!')
    return render(request, 'participante/search_by_cpf.html')

def participante_list(request):
    f = ParticipanteFilter(request.GET, queryset=Profile.objects.all())
    return render(request, 'participante/template.html', {'filter': f})

def register2(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST,
                                              files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return render(request,
                          'participante/register_done2.html',
                          {'new_user': new_profile})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
    return render(request, 'participante/register.html', {'user_form': user_form, 'profile_form': profile_form})

def homepage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active and user.is_superuser:
                    login(request, user)
                    return render(request, 'lojista/dashboard.html')
                elif user.is_active:
                    login(request, user)
                    return render(request, 'participante/dashboard.html')
            else:
                login_form = LoginForm()
                return render(request, 'participante/index.html', {'section': 'homepage', 'lf': login_form})
    else:
        login_form = LoginForm()
    return render(request, 'participante/index.html', {'section': 'homepage', 'lf': login_form})

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
        profile_form = ProfileRegistrationForm(request.POST,
                                              files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return render(request,
                          'participante/register_done.html',
                          {'new_user': new_profile})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
    return render(request, 'participante/register2.html', {'user_form': user_form, 'profile_form': profile_form})


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
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    profile = get_object_or_404(Profile, user=user)
    docs_list = DocumentoFiscal.objects.filter(user=user)
    return render(request, 'participante/detail.html', {'section': 'people','user': profile, 'docs': docs_list})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, username):
    if request.method == 'POST':
        instance_user = get_object_or_404(User, username=username)
        instance_profile = get_object_or_404(Profile, user=instance_user)
        profile_form = ProfileEditForm(instance=instance_profile,
                                        data=request.POST,
                                        files=request.FILES)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Participante validado com sucesso')
        else:
            messages.error(request, 'Erro na validação do Participante')
    else:
        instance_user = get_object_or_404(User, username=username)
        instance_profile = get_object_or_404(Profile, user=instance_user)
        profile_form = ProfileEditForm(instance=instance_profile)
    return render(request, 'participante/editbyoperador.html', {'profile_form': profile_form})

@login_required
def adddocfiscal(request):
    if request.method == 'POST':
        documentoFiscal_form = UserAddFiscalDocForm(request.POST,
                                                    files=request.FILES)
        cnpj = documentoFiscal_form['lojista_cnpj'].value()
        lojista = get_object_or_404(Lojista, CNPJLojista=cnpj)
        user = request.user
        if documentoFiscal_form.is_valid():
            # Create a new document object but avoid saving it yet
            new_documentoFiscal = documentoFiscal_form.save(commit=False)
            # Set the user
            new_documentoFiscal.user = user
            new_documentoFiscal.lojista = lojista
            # Save the doc object
            new_documentoFiscal.save()
            return render(request,
                          'participante/doc_fiscal_done.html',
                          {'new_documentoFiscal': new_documentoFiscal})
    else:
        documentoFiscal_form = UserAddFiscalDocForm()
    return render(request, 'participante/doc_fiscal_add.html', {'documentoFiscal_form': documentoFiscal_form})

@login_required
def adddocfiscalbyop(request, username):
    if request.method == 'POST':
        documentoFiscal_form = UserAddFiscalDocForm(request.POST,
                                                    files=request.FILES)
        cnpj = documentoFiscal_form['lojista_cnpj'].value()
        lojista = get_object_or_404(Lojista, CNPJLojista=cnpj)
        user = get_object_or_404(User, username=username)
        if documentoFiscal_form.is_valid():
            # Create a new document object but avoid saving it yet
            new_documentoFiscal = documentoFiscal_form.save(commit=False)
            # Set the user
            new_documentoFiscal.user = user
            new_documentoFiscal.lojista = lojista
            # Save the doc object
            new_documentoFiscal.save()
            return render(request,
                          'participante/doc_fiscal_done_op.html',
                          {'new_documentoFiscal': new_documentoFiscal, 'participante': user})
    else:
        documentoFiscal_form = UserAddFiscalDocForm()
        user = get_object_or_404(User, username=username)
    return render(request, 'participante/doc_fiscal_add_op.html', {'documentoFiscal_form': documentoFiscal_form, 'participante': user})

@login_required
def doclist(request):
    docs_list = DocumentoFiscal.objects.filter(user=request.user)
    docs_filter = DocFilter(request.GET, queryset=docs_list)
    return render(request, 'participante/list_doc_fiscal.html', {'filter': docs_filter,
                                                                   'section':'docsfiscais'})

@login_required
def editdocfiscal(request, numerodocumento):
    if request.method == 'POST':
        instance = get_object_or_404(DocumentoFiscal, numeroDocumento=numerodocumento)
        documentofiscal_form = DocumentoFiscalEditForm(instance=instance,data=request.POST,
                                                                        files=request.FILES)
        if documentofiscal_form.is_valid():
            documentofiscal_form.save()
            messages.success(request, 'Documento Fiscal atualizado com sucesso')
        else:
            messages.error(request, 'Erro na atualização do Documento Fiscal')
    else:
        instance = get_object_or_404(DocumentoFiscal, numeroDocumento=numerodocumento)
        documentofiscal_form = DocumentoFiscalEditForm(instance=instance)
    return render(request, 'participante/doc_fiscal_edit.html', {'documentofiscal_form': documentofiscal_form})

@login_required
def validadocfiscal(request, numerodocumento):
    if request.method == 'POST':
        instance = get_object_or_404(DocumentoFiscal, numeroDocumento=numerodocumento)
        documentofiscal_form = DocumentoFiscalValidaForm(instance=instance,data=request.POST,
                                                                    files=request.FILES)
        profile = get_object_or_404(Profile, user= instance.user)
        docs = DocumentoFiscal.objects.filter(user=instance.user)
        if documentofiscal_form.is_valid():
            new_doc = documentofiscal_form.save()
            qtde = int(new_doc.get_cupons())
            for x in range(qtde):
                cupom = Cupom.objects.create(documentoFiscal=new_doc, user=new_doc.user, operador=request.user)
            messages.success(request, 'Documento Fiscal validado com sucesso')
            return render(request, 'participante/detail.html', {'section': 'people','user': profile, 'docs': docs})
        else:
            messages.error(request, 'Erro na validação do Documento Fiscal')
    else:
        instance = get_object_or_404(DocumentoFiscal, numeroDocumento=numerodocumento)
        documentofiscal_form = DocumentoFiscalValidaForm(instance=instance)
    return render(request, 'participante/doc_fiscal_valida.html', {'documentofiscal_form': documentofiscal_form, 'doc':instance})


@login_required
def dashboard(request):
    if request.user.is_superuser: return render(request, 'lojista/dashboard.html', {'section': 'lojista'})
    docs = DocumentoFiscal.objects.filter(user=request.user)
    return render(request, 'participante/dashboard.html', {'section': 'dashboard','docs': docs})

@login_required
def lojista(request):
    return render(request, 'not_found.html', {'section': 'coupons'})

@login_required
def coupons(request):
    return render(request, 'participante/coupons.html', {'section': 'coupons'})

@login_required
def premios(request):
    return render(request, 'participante/premios.html', {'section': 'premios'})
