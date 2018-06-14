from django.contrib import admin
from .models import Cupom
# Register your models here.
class CupomAdmin(admin.ModelAdmin):
    list_display = ('numeroCupom', 'user', 'documentoFiscal', 'operador', 'dataCriacao', 'impresso', 'dataImpressao')

admin.site.register(Cupom, CupomAdmin)
