from django.contrib import admin
from .models import Profile, DocumentoFiscal

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'CHOICES_SEXO', 'nome', 'RG', 'CPF', 'sexo', 'foneFixo',
                    'foneCelular1', 'foneCelular2', 'foneCelular3', 'whatsapp', 'facebook', 'twitter',
                    'endereco', 'enderecoNumero', 'enderecoComplemento', 'bairro', 'cidade', 'estado', 'CEP', 'cadastradoPor',
                    'dataCadastro', 'observacao', 'pergunta', 'ativo']

class DocumentoFiscalAdmin(admin.ModelAdmin):
    list_display = ['user', 'numeroDocumento', 'lojista', 'vendedor', 'dataDocumento', 'valorDocumento', 'compradoREDE', 'compradoMASTERCARD',
                    'photo', 'valorREDE','valorMASTERCARD', 'valorVirtual', 'dataCadastro', 'cadastradoPor']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(DocumentoFiscal, DocumentoFiscalAdmin)
