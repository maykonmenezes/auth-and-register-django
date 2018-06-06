# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='CPF',
            field=models.CharField(max_length=14, unique=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='RG',
            field=models.CharField(max_length=12, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='dataAtual',
            field=models.DateField(verbose_name='Data Atual', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='enderecoComplemento',
            field=models.CharField(verbose_name='Complemento', max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='foneCelular1',
            field=models.CharField(verbose_name='Celular1', max_length=15, blank=True, help_text='ex. (85)98888-8675'),
        ),
        migrations.AddField(
            model_name='profile',
            name='foneFixo',
            field=models.CharField(verbose_name='Telefone Fixo', max_length=15, blank=True, help_text='ex. (85)3212-0000'),
        ),
        migrations.AddField(
            model_name='profile',
            name='nome',
            field=models.CharField(max_length=70, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='pergunta',
            field=models.TextField(verbose_name='Observação', max_length=1000, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='sexo',
            field=models.CharField(verbose_name='Sexo', max_length=1, blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], help_text='ex. M ou F'),
        ),
    ]
