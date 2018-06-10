from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Lojista, RamoAtividade


class LojistaRegistrationForm(forms.ModelForm):

    class Meta:
        model = Lojista
        fields = '__all__'

class RamoAtividadeRegistrationForm(forms.ModelForm):

    class Meta:
        model = RamoAtividade
        fields = '__all__'
