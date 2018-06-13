from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import DocumentoFiscal


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha*', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Senha novamente*', widget=forms.PasswordInput)
    username = forms.CharField(label='Nome de usuario*', help_text='Ex: nomeSobrenome2')
    first_name = forms.CharField(label='Nome Completo*', widget=forms.TextInput(attrs={'scope' : 'col'}))
    email = forms.EmailField(label='Email*', help_text='exemplo@gmail.com')
    CPF = forms.CharField(label='CPF*')
    RG = forms.CharField( label='RG*')
    sexo = forms.CharField(label='Sexo')
    foneFixo = forms.CharField(label='Telefone Fixo', required=False, help_text='(DDD) 9 XXXX - XXXX')
    foneCelular1 = forms.CharField(label='Celular*', help_text='(DDD) 9 XXXX - XXXX')
    foneCelular2 = forms.CharField(label='Celular 2', required=False, help_text='(DDD) 9 XXXX - XXXX')
    foneCelular3 = forms.CharField(label='Celular 3', required=False, help_text='(DDD) 9 XXXX - XXXX')
    whatsapp = forms.CharField(label='Whatsapp*', help_text='(DDD) 9 XXXX - XXXX')
    facebook = forms.CharField(label='Facebook', required=False)
    twitter = forms.CharField(label='Twitter', required=False, initial='@', help_text='Ex: @seuUsuario')
    endereco = forms.CharField(label='Endereço*', help_text='Ex: Rua Sebastiao Ferreira')
    enderecoNumero = forms.CharField(label='Número*', help_text='O numero da sua casa')
    EnderecoComplemento = forms.CharField(label='Complemento', required=False, help_text='Ponto de referencia')
    bairro = forms.CharField(label='Bairro*')
    cidade = forms.CharField(label='Cidade*')
    estado = forms.CharField(label='Estado*')
    cep = forms.CharField(label='Cep*')
    pergunta = forms.CharField(label='Qual a maior liquidação de Teresina?')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'CPF', 'RG', 'sexo', 'foneFixo', 'foneCelular1', 'foneCelular2', 'foneCelular3',
        'whatsapp', 'facebook', 'twitter', 'endereco', 'enderecoNumero', 'EnderecoComplemento', 'bairro', 'cidade', 'estado', 'cep', 'pergunta' )


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

    vendedor = forms.CharField(label='Vendedor', required=False)
    numeroDocumento = forms.CharField(label='Número do Documento')
    dataDocumento = forms.DateField(label='Data do documento')
    valorDocumento = forms.DecimalField(label='Valor do documento')
    compradoREDE = forms.BooleanField(label='Compra na REDE?')
    valorREDE = forms.DecimalField(label='Valor REDE')
    photo = forms.ImageField(label='Foto do documento', required=False)
    compradoMASTERCARD = forms.BooleanField(label='Compra com MASTERCARD?')
    valorMASTERCARD = forms.DecimalField(label='Valor MASTERCARD')
    class Meta:
        model = DocumentoFiscal
        fields = ('numeroDocumento', 'dataDocumento', 'valorDocumento', 'compradoREDE','valorREDE', 'compradoMASTERCARD', 'valorMASTERCARD',
        'photo', 'vendedor')

class DocumentoFiscalEditForm(forms.ModelForm):
    class Meta:
        model = DocumentoFiscal
        fields = '__all__'
        

class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Data de Nascimento')
    photo = forms.ImageField(label='Foto')
    RG = forms.CharField( label='RG')
    dataAtual = forms.DateField(label='Data Atual')  #mudar depois para nao colocar a data atual
    sexo = forms.CharField(label='Sexo')
    foneFixo = forms.CharField(label='Telefone Fixo')
    foneCelular1 = forms.CharField(label='Celular')
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo', 'RG', 'dataAtual', 'sexo', 'foneFixo', 'foneCelular1' )
