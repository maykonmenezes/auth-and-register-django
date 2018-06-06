from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    nome = models.CharField(max_length=70, blank=True)
    RG = models.CharField(max_length=12, blank=True)
    dataAtual = models.DateField(verbose_name=u'Data Atual', null=True, blank=True)  #mudar depois para nao colocar a data atual
    sexo = models.CharField(verbose_name=u'Sexo', max_length=1, choices=CHOICES_SEXO, blank=True, help_text=u'ex. M ou F')
    foneFixo = models.CharField(verbose_name=u'Telefone Fixo', max_length=15, blank=True, help_text=u'ex. (85)3212-0000')
    foneCelular1 = models.CharField(verbose_name=u'Celular1', max_length=15, blank=True, help_text=u'ex. (85)98888-8675')
    enderecoComplemento = models.CharField(verbose_name=u'Complemento', max_length=30, blank=True)
    pergunta = models.TextField(verbose_name=u'Observação', max_length=1000, blank=True, null=True ) #, widget=forms.Textarea(attrs={'placeholder': 'Escreva aqui alguma observação caso seja necessário.'}))
    Ativo = models.BooleanField(default=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
