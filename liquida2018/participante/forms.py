from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Cpf
from .models import DocumentoFiscal
from localflavor.br.forms import *
from localflavor.br.br_states import STATE_CHOICES


class SearchByCpfForm(forms.Form):
    CPF = BRCPFField(label="CPF",required=True, max_length=14, min_length=11, widget=forms.TextInput(attrs={'placeholder':'CPF*',
                                                                                                               'class':'cpf'}))
    class Meta:
        model = Profile
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite seu usuario', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha', 'class':'form-control'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Senha*'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder':'Confirmação de senha*'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Usúario*'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email*'}))
    class Meta:
        model = User
        fields = ('username', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha digitada não é a mesma.')
        return cd['password2']

class ProfileRegistrationForm(forms.ModelForm):
    CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))
    sexo = forms.ChoiceField(choices=CHOICES_SEXO, widget=forms.Select(attrs={'id' : 'sexo'}))
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    pergunta = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Sua resposta'}))
    nome = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Nome Completo*'}))
    RG = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'RG*'}))
    CPF = BRCPFField(required=True, max_length=14, min_length=11, widget=forms.TextInput(attrs={'placeholder':'CPF*',
                                                                                                'class':'cpf'}))
    foneCelular1 = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Celular*',
                                                                                  'class': 'phone_with_ddd'}))
    whatsapp = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Whatsapp',
                                                                                  'class': 'phone_with_ddd'}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Facebook'}))
    twitter = forms.CharField( required=False, widget=forms.TextInput(attrs={'placeholder':'Twitter'}) )
    endereco = forms.CharField( required=True, widget=forms.TextInput(attrs={'placeholder':'Endereço*'}))
    enderecoNumero = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nº*'}))
    enderecoComplemento = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Complemento'}))
    bairro = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Bairro*'}))
    cidade = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Cidade*'}))
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    CEP = BRZipCodeField(label='Cep*' , widget=forms.TextInput(attrs={'class':'cep', 'placeholder':'CEP*'}))
    pergunta = forms.CharField( required=True, widget=forms.TextInput(attrs={'placeholder':'Liquida Teresina'}))
    class Meta:
        model = Profile
        fields = ('nome', 'RG', 'CPF', 'sexo', 'foneFixo', 'foneCelular1', 'foneCelular2', 'foneCelular3',
                  'whatsapp','facebook','twitter','endereco','enderecoNumero','enderecoComplemento', 'estado',
                  'cidade','bairro','CEP','pergunta' )
        exclude = ('user', 'dataCadastro', 'cadastradoPor', 'ativo', 'pendente')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha digitada não é a mesma.')
        return cd['password2']


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'ativo': forms.HiddenInput,
        }


class UserAddCoupom(forms.ModelForm):
    numeroDoCupom = forms.CharField(label='Numero do cupom')
    valorDoCupom = forms.DecimalField(label='Valor do cupom')

class UserAddFiscalDocForm(forms.ModelForm):
    lojista_cnpj = BRCNPJField(label='CNPJ da loja*', required=True, max_length=18, widget=forms.TextInput(attrs={'class':'cnpj'}))
    dataDocumento = forms.DateField(label='Data*',widget=forms.TextInput(attrs={ 'class':'date'}))
    valorDocumento = forms.DecimalField(label='Valor*')
    numeroDocumento = forms.CharField(label='Número do documento*')
    photo = forms.ImageField(label='Documento fiscal', required=False)
    photo2 = forms.ImageField(label='Comprovante do cartão', required=False)
    class Meta:
        model = DocumentoFiscal
        fields = ('lojista_cnpj', 'vendedor', 'numeroDocumento', 'dataDocumento', 'valorDocumento', 'photo', 'photo2')
        widgets = {
            #'lojista': forms.HiddenInput,
            'compradoREDE': forms.HiddenInput,
            'compradoMASTERCARD': forms.HiddenInput,
            'valorREDE': forms.HiddenInput,
            'valorMASTERCARD': forms.HiddenInput,
            'valorVirtual': forms.HiddenInput,
        }

class DocumentoFiscalEditForm(forms.ModelForm):
    class Meta:
        model = DocumentoFiscal
        fields = '__all__'
        widgets = {
            'compradoREDE': forms.HiddenInput,
            'compradoMASTERCARD': forms.HiddenInput,
            'valorREDE': forms.HiddenInput,
            'valorMASTERCARD': forms.HiddenInput,
            'valorVirtual': forms.HiddenInput,
        }

class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Data de Nascimento',required=False)
    photo = forms.ImageField(label='Foto')
    CPF = BRCPFField(label="CPF",required=True, max_length=14, min_length=11)
    RG = forms.CharField( label='RG*')
    sexo = forms.CharField(label='Sexo*')
    foneFixo = forms.CharField(label='Telefone Fixo', required=False, help_text='(DDD) 9 XXXX - XXXX')
    foneCelular1 = forms.CharField(label='Celular*', help_text='(DDD) 9 XXXX - XXXX')
    foneCelular2 = forms.CharField(label='Celular 2', required=False, help_text='(DDD) 9 XXXX - XXXX')
    foneCelular3 = forms.CharField(label='Celular 3', required=False, help_text='(DDD) 9 XXXX - XXXX')
    whatsapp = forms.CharField(label='Whatsapp', required=False, help_text='(DDD) 9 XXXX - XXXX')
    facebook = forms.CharField(label='Facebook', required=False)
    twitter = forms.CharField(label='Twitter', required=False, initial='@', help_text='Ex: @seuUsuario')
    endereco = forms.CharField(label='Endereço*', help_text='Ex: Rua Sebastiao Ferreira')
    enderecoNumero = forms.CharField(label='Número*', help_text='O numero da sua casa')
    enderecoComplemento = forms.CharField(label='Complemento', required=False, help_text='Ponto de referencia')
    bairro = forms.CharField(label='Bairro*')
    cidade = forms.CharField(label='Cidade*')
    estado = forms.ChoiceField(required=True, choices=STATE_CHOICES, widget=forms.Select(attrs={'id' : 'estados'}))
    cep = BRZipCodeField(label='Cep*')
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'RG' , 'CPF','sexo', 'foneFixo', 'foneCelular1', 'foneCelular2', 'foneCelular3',
        'whatsapp', 'facebook', 'twitter', 'endereco', 'enderecoNumero', 'enderecoComplemento', 'bairro', 'cidade','cep' )
