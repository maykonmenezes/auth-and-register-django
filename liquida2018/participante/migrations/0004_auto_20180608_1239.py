# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0003_remove_profile_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoFiscal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('vendedor', models.CharField(verbose_name='Nome do Vendedor', max_length=50, blank=True, null=True)),
                ('numeroDocumento', models.CharField(verbose_name='Número do Documento', max_length=12)),
                ('dataDocumento', models.DateField(verbose_name='Data do Documento')),
                ('valorDocumento', models.DecimalField(verbose_name='Valor do Documento', default=0, max_digits=7, decimal_places=2)),
                ('compradoREDE', models.BooleanField(verbose_name='Compra na REDE', default=False)),
                ('valorREDE', models.DecimalField(verbose_name='Valor na REDE', blank=True, default=0, editable=False, max_digits=7, decimal_places=2)),
                ('photo', models.ImageField(blank=True, upload_to='do/%Y/%m/%d')),
                ('compradoMASTERCARD', models.BooleanField(verbose_name='Compra com MASTERCARD', default=False)),
                ('valorMASTERCARD', models.DecimalField(verbose_name='Valor no MASTERCARD', blank=True, default=0, editable=False, max_digits=7, decimal_places=2)),
                ('valorVirtual', models.DecimalField(verbose_name='Valor com Bonificações', blank=True, default=0, editable=False, max_digits=7, decimal_places=2)),
                ('dataCadastro', models.DateTimeField(verbose_name='Cadastrado em', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Documento Fiscal',
                'verbose_name_plural': 'Documentos Fiscais',
            },
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Ativo',
            new_name='ativo',
        ),
        migrations.AddField(
            model_name='profile',
            name='CEP',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Email',
            field=models.EmailField(max_length=60, blank=True, help_text='ex. nome@email.com'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Facebook',
            field=models.CharField(max_length=50, blank=True, help_text='ex. fb.com/nomenofacebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='FoneCelular2',
            field=models.CharField(verbose_name='Celular2', max_length=15, blank=True, help_text='ex. (85)98888-8675'),
        ),
        migrations.AddField(
            model_name='profile',
            name='FoneCelular3',
            field=models.CharField(verbose_name='Celular3', max_length=15, blank=True, help_text='ex. (85)98888-8675'),
        ),
        migrations.AddField(
            model_name='profile',
            name='Twitter',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Whatsapp',
            field=models.CharField(max_length=15, blank=True, help_text='ex. (85)98888-8675'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bairro',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cidade',
            field=models.CharField(max_length=50, blank=True, default='Teresina'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dataCadastro',
            field=models.DateTimeField(verbose_name='Cadastrado em', default=datetime.datetime(2018, 6, 8, 15, 39, 25, 882145, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='endereco',
            field=models.CharField(verbose_name='Endereço', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='enderecoNumero',
            field=models.CharField(verbose_name='Nº Endereço', max_length=8, blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='estado',
            field=models.CharField(max_length=2, blank=True, default='PI'),
        ),
        migrations.AddField(
            model_name='profile',
            name='observacao',
            field=models.TextField(verbose_name='Observação', max_length=1000, blank=True, null=True),
        ),
    ]
