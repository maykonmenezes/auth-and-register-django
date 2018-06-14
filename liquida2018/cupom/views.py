from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import AddCupomForm, EditCupomForm
from .models import Cupom

@login_required
@user_passes_test(lambda u: u.is_superuser)
def detail(request):
    return render(request, 'cupom/detail.html', {'section': 'cupom-detail'})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def addcupom(request, numerodocumento):
    if request.method == 'POST':
        cupom_form = AddCupomForm(request.POST)
        doc = get_object_or_404(DocumentoFiscal, numeroDocumento=numerodocumento)
        if cupom_form.is_valid():
            new_cupom = cupom_form.save(commit=False)
            new_cupom.documentoFiscal = doc
            new_cupom.user = doc.user
            new_cupom.save()
            messages.success(request, 'Cupom gerado com sucesso')
    else:
        messages.success(request, 'Erro ao gerar o cupom')

@login_required
@user_passes_test(lambda u: u.is_superuser)
def cupomlist(request, username):
    user = get_object_or_404(User, username=username)
    cupons = Cupom.objects.filter(user)
    return render(request, 'cupom/list.html', {'section': 'cuponslist',
                                                      'cupons': cupons})
@login_required
@user_passes_test(lambda u: u.is_superuser)
def printCupom(request):
    print('imprimir')
