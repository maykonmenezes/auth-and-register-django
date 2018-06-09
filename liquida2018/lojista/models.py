from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class RamoAtividade(models.Model):
    """
    Model representando o ramo de atividade.
    """
    Atividade = models.CharField(max_length=80, help_text='Informe o Ramo de Atividade. (exemplo: alimentação, vestuário, restaurante, etc.)')
    DataCadastro    = models.DateTimeField(verbose_name=u'Cadastrado em', auto_now_add=True, editable=False)   #nao vai aparecer na tela
    #CadastradoPor   = CurrentUserField(verbose_name=u'Cadastrado Por')
#    DataAlteracao   = models.DateTimeField(verbose_name=u'Alterado em', auto_now_add=True) #nao vai aparecer na tela
#    AlteradoPor_Id   = models.ForeignKey(User, blank=False, related_name='Cadastrado_por', editable=False, default=current_user.get_current_user)
    Ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['Atividade']
        verbose_name = (u'Ramo de Atividade')
        verbose_name_plural = (u'Ramos de Atividades')

    def __str__(self):
        """
        String representando o Model object (in Admin site etc.)
        """
        return self.Atividade


class Lojista(models.Model):
    CNPJLojista     = models.CharField(verbose_name=u'CNPJ do Lojista', max_length=18, blank=False, null=True, unique=True, help_text=u'ex. 00.000.000/0000-00')
    IELojista       = models.CharField(verbose_name=u'Inscrição Estadual', max_length=14, blank=True)
    RazaoLojista    = models.CharField(verbose_name=u'Razão Social', max_length=70, blank=True, null=True, help_text=u'Razão Social')
    FantasiaLojista = models.CharField(verbose_name=u'Nome Fantasia', max_length=70, blank=False, help_text=u'Nome Fantasia')
    RamoAtividade   = models.ForeignKey('RamoAtividade', verbose_name=u'Ramo de Atividade', on_delete=models.SET_NULL, null=True)
    DataCadastro    = models.DateTimeField(verbose_name=u'Cadastrado em', auto_now_add=True, editable=False)   #nao vai aparecer na tela
    #CadastradoPor   = CurrentUserField(verbose_name=u'Cadastrado Por')
#    CadastradoPor_Id = models.ForeignKey(User, editable=False, default=User.pk, on_delete=models.SET_NULL, null=True)
#    CadastradoPor_Id = models.ForeignKey(User, blank=False, related_name='Cadastrado_por', editable=False, default=current_user.get_current_user)
#    DataAlteracao   = models.DateTimeField(verbose_name=u'Alterado em', auto_now_add=True) #nao vai aparecer na tela
#    AlteradoPor_Id   = models.ForeignKey(User, blank=False, related_name='Cadastrado_por', editable=False, default=current_user.get_current_user)
    Ativo           = models.BooleanField(default=True)


    class Meta:
        ordering = ['FantasiaLojista']
        verbose_name = (u'Lojista')
        verbose_name_plural = (u'Lojistas')


    def __str__(self):
        """
        String representando o Objeto Participante.
        """
        return self.FantasiaLojista
