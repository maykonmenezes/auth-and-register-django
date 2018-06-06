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
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('A senha digitada não é a mesma.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome Completo')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='Email')
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(label='Data de Nascimento')
    photo = forms.ImageField(label='Foto')
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
