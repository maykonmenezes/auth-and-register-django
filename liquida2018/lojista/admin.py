from django.contrib import admin
from .models import Lojista, RamoAtividade

class LojistaAdmin(admin.ModelAdmin):
    list_display = ['CNPJLojista', 'IELojista', 'razaoLojista', 'fantasiaLojista',
                        'ramoAtividade', 'dataCadastro', 'CadastradoPor', 'ativo' ]

class RamoAtividadeAdmin(admin.ModelAdmin):
    list_display = ['atividade', 'dataCadastro', 'CadastradoPor', 'ativo']

admin.site.register(Lojista, LojistaAdmin)
admin.site.register(RamoAtividade, RamoAtividadeAdmin)
