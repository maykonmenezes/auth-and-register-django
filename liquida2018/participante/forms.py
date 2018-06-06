from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Senha novamente', widget=forms.PasswordInput)
    username = forms.CharField(label='Usuario')
    first_name = forms.CharField(label='Nome Completo')
    email = forms.CharField(label='Email')
    CPF = forms.CharField(label='CPF')
    RG = forms.CharField( label='RG')
    dataAtual = forms.DateField(label='Data Atual')  #mudar depois para nao colocar a data atual
    sexo = forms.CharField(label='Sexo')
    foneFixo = forms.CharField(label='Telefone Fixo')
    foneCelular1 = forms.CharField(label='Celular')
    pergunta = forms.CharField(label='Qual a maior liquidação de Teresina?')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'CPF', 'RG', 'dataAtual', 'sexo', 'foneFixo', 'foneCelular1', 'pergunta' )


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha digitada não é a mesma.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome Completo')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='Email')
    CPF = forms.CharField(label='CPF')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id')

class UserAddCoupom(forms.ModelForm):
    numeroDoCupom = forms.CharField(label='Numero do cupom')
    valorDoCupom = forms.DecimalField(label='Valor do cupom')


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
