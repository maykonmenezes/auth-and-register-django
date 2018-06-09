# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lojista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('CNPJLojista', models.CharField(verbose_name='CNPJ do Lojista', max_length=18, unique=True, null=True, help_text='ex. 00.000.000/0000-00')),
                ('IELojista', models.CharField(verbose_name='Inscrição Estadual', max_length=14, blank=True)),
                ('RazaoLojista', models.CharField(verbose_name='Razão Social', max_length=70, blank=True, null=True, help_text='Razão Social')),
                ('FantasiaLojista', models.CharField(verbose_name='Nome Fantasia', max_length=70, help_text='Nome Fantasia')),
                ('DataCadastro', models.DateTimeField(verbose_name='Cadastrado em', auto_now_add=True)),
                ('Ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Lojista',
                'verbose_name_plural': 'Lojistas',
                'ordering': ['FantasiaLojista'],
            },
        ),
        migrations.CreateModel(
            name='RamoAtividade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Atividade', models.CharField(max_length=80, help_text='Informe o Ramo de Atividade. (exemplo: alimentação, vestuário, restaurante, etc.)')),
                ('DataCadastro', models.DateTimeField(verbose_name='Cadastrado em', auto_now_add=True)),
                ('Ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ramo de Atividade',
                'verbose_name_plural': 'Ramos de Atividades',
                'ordering': ['Atividade'],
            },
        ),
        migrations.AddField(
            model_name='lojista',
            name='RamoAtividade',
            field=models.ForeignKey(verbose_name='Ramo de Atividade', null=True, on_delete=django.db.models.deletion.SET_NULL, to='lojista.RamoAtividade'),
        ),
    ]
