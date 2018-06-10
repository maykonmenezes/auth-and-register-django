# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojista', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lojista',
            options={'verbose_name': 'lojista', 'verbose_name_plural': 'lojistas', 'ordering': ['fantasiaLojista']},
        ),
        migrations.AlterModelOptions(
            name='ramoatividade',
            options={'verbose_name': 'ramo de Atividade', 'verbose_name_plural': 'ramos de Atividades', 'ordering': ['atividade']},
        ),
        migrations.RenameField(
            model_name='lojista',
            old_name='Ativo',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='lojista',
            old_name='DataCadastro',
            new_name='dataCadastro',
        ),
        migrations.RenameField(
            model_name='lojista',
            old_name='FantasiaLojista',
            new_name='fantasiaLojista',
        ),
        migrations.RenameField(
            model_name='lojista',
            old_name='RamoAtividade',
            new_name='ramoAtividade',
        ),
        migrations.RenameField(
            model_name='lojista',
            old_name='RazaoLojista',
            new_name='razaoLojista',
        ),
        migrations.RenameField(
            model_name='ramoatividade',
            old_name='Atividade',
            new_name='atividade',
        ),
        migrations.RenameField(
            model_name='ramoatividade',
            old_name='Ativo',
            new_name='ativo',
        ),
        migrations.RenameField(
            model_name='ramoatividade',
            old_name='DataCadastro',
            new_name='dataCadastro',
        ),
    ]
