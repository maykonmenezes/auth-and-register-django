from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from lojista.models import Lojista
from django.utils.text import slugify
from django.core.urlresolvers import reverse
#from django.contrib.auth import get_user_model

#from django_currentuser.db.models import CurrentUserField

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
    FoneCelular2 = models.CharField(verbose_name=u'Celular2', max_length=15, blank=True, help_text=u'ex. (85)98888-8675')
    FoneCelular3 = models.CharField(verbose_name=u'Celular3', max_length=15, blank=True, help_text=u'ex. (85)98888-8675')
    Whatsapp = models.CharField(max_length=15, blank=True, help_text=u'ex. (85)98888-8675')
    Email = models.EmailField(max_length=60, blank=True, help_text=u'ex. nome@email.com')
    Facebook = models.CharField(max_length=50, blank=True , help_text=u'ex. fb.com/nomenofacebook')
    Twitter = models.CharField(max_length=50, blank=True)
    endereco = models.CharField(verbose_name=u'Endereço', max_length=50, blank=True)
    enderecoNumero = models.CharField(verbose_name=u'Nº Endereço', max_length=8, blank=True)
    enderecoComplemento = models.CharField(verbose_name=u'Complemento', max_length=30, blank=True)
    bairro = models.CharField(max_length=40, blank=True)
    cidade = models.CharField(max_length=50, blank=True, default=u'Teresina')
    estado = models.CharField(max_length=2, blank=True, default=u'PI')
    CEP = models.CharField(max_length=10, blank=True)
    observacao = models.TextField(verbose_name=u'Observação', max_length=1000, blank=True, null=True ) #, widget=forms.Textarea(attrs={'placeholder': 'Escreva aqui alguma observação caso seja necessário.'}))
    dataCadastro = models.DateTimeField(verbose_name=u'Cadastrado em', auto_now_add=True, editable=False)   #nao vai aparecer na tela
    #CadastradoPor = CurrentUserField(verbose_name=u'Cadastrado Por')
    pergunta = models.TextField(verbose_name=u'Pergunta', max_length=50, blank=True, null=True ) #, widget=forms.Textarea(attrs={'placeholder': 'Escreva aqui alguma observação caso seja necessário.'}))
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return 'Nome completo {}'.format(self.user.username)


class DocumentoFiscal(models.Model):
    #Lojista_Id = models.ForeignKey('Lojista', verbose_name=u'Loja', on_delete=models.SET_NULL, null=True)
    #Participante_Id = models.ForeignKey('Participante', default=1, verbose_name=u'Participante', on_delete=models.SET_NULL, null=True)
    user =  models.ForeignKey(User, related_name='rel_username',editable=False)
    lojista =  models.ForeignKey(Lojista, related_name='rel_lojista', null=False, blank=False, default=1)
    vendedor = models.CharField(verbose_name=u'Nome do Vendedor', max_length=50, blank=True, null=True)
    numeroDocumento = models.CharField(verbose_name=u'Número do Documento', max_length=12, blank=False, null=False, unique=True)
    dataDocumento = models.DateField(verbose_name=u'Data do Documento', null=False, blank=False)
    valorDocumento = models.DecimalField(verbose_name=u'Valor do Documento', max_digits=7, decimal_places=2, blank=False, default=0)
    compradoREDE = models.BooleanField(verbose_name=u'Compra na REDE', default=False)
    valorREDE = models.DecimalField(verbose_name=u'Valor na REDE', max_digits=7, decimal_places=2, editable=False, blank=True, default=0)   #depois posso nao mostrar
    photo = models.ImageField(upload_to='docs/%Y/%m/%d', blank=True)
    compradoMASTERCARD = models.BooleanField(verbose_name=u'Compra com MASTERCARD', default=False)
    valorMASTERCARD = models.DecimalField(verbose_name=u'Valor no MASTERCARD', max_digits=7, decimal_places=2, editable=False, blank=True, default=0)   #depois posso nao mostrar
    valorVirtual = models.DecimalField(verbose_name=u'Valor com Bonificações', max_digits=7, decimal_places=2, editable=False, blank=True, default=0)   #depois posso nao mostrar
    dataCadastro = models.DateTimeField(verbose_name=u'Cadastrado em', auto_now_add=True, editable=False)
    #CadastradoPor = CurrentUserField(verbose_name=u'Cadastrado Por')
    #slug = models.SlugField(max_length=200, blank=True)
    exclude=('valorREDE','valorMASTERCARD','valorVirtual')


    class Meta:
        #ordering = ['Participante_Id', 'NumeroDocumento']
        verbose_name = (u'Documento Fiscal')
        verbose_name_plural = (u'Documentos Fiscais')

    def get_absolute_url(self):
        return reverse('documentosficais:detail', args=[self.numeroDocumento, self.slug])

#    def soma_valor(self, ValorDocumento, CompradoREDE, CompradoMASTERCARD):
    def soma_valor(self):
        soma=0
        if self.compradoREDE.check():
            soma = self.valorDocumento * 2
            return soma
        else:
            if self.compradoMASTERCARD.check():
                soma = self.valorDocumento * 3
                return soma
