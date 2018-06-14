# Generated by Django 2.0.6 on 2018-06-14 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lojista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoFiscal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendedor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nome do Vendedor')),
                ('numeroDocumento', models.CharField(max_length=12, unique=True, verbose_name='Número do Documento')),
                ('dataDocumento', models.DateField(verbose_name='Data do Documento')),
                ('valorDocumento', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Valor do Documento')),
                ('compradoREDE', models.BooleanField(default=False, verbose_name='Compra na REDE')),
                ('valorREDE', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=7, verbose_name='Valor na REDE')),
                ('photo', models.ImageField(blank=True, upload_to='docs/%Y/%m/%d')),
                ('compradoMASTERCARD', models.BooleanField(default=False, verbose_name='Compra com MASTERCARD')),
                ('valorMASTERCARD', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=7, verbose_name='Valor no MASTERCARD')),
                ('valorVirtual', models.DecimalField(blank=True, decimal_places=2, default=0, editable=False, max_digits=7, verbose_name='Valor com Bonificações')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('CadastradoPor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cadastrado Por')),
                ('lojista', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='rel_lojista', to='lojista.Lojista')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='rel_username', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Documento Fiscal',
                'verbose_name_plural': 'Documentos Fiscais',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('nome', models.CharField(blank=True, max_length=70)),
                ('RG', models.CharField(blank=True, max_length=12)),
                ('CPF', models.CharField(blank=True, max_length=12)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], help_text='ex. M ou F', max_length=1, verbose_name='Sexo')),
                ('foneFixo', models.CharField(blank=True, help_text='ex. (85)3212-0000', max_length=15, verbose_name='Telefone Fixo')),
                ('foneCelular1', models.CharField(blank=True, help_text='ex. (85)98888-8675', max_length=15, verbose_name='Celular1')),
                ('FoneCelular2', models.CharField(blank=True, help_text='ex. (85)98888-8675', max_length=15, verbose_name='Celular2')),
                ('FoneCelular3', models.CharField(blank=True, help_text='ex. (85)98888-8675', max_length=15, verbose_name='Celular3')),
                ('Whatsapp', models.CharField(blank=True, help_text='ex. (85)98888-8675', max_length=15)),
                ('Email', models.EmailField(blank=True, help_text='ex. nome@email.com', max_length=60)),
                ('Facebook', models.CharField(blank=True, help_text='ex. fb.com/nomenofacebook', max_length=50)),
                ('Twitter', models.CharField(blank=True, max_length=50)),
                ('endereco', models.CharField(blank=True, max_length=50, verbose_name='Endereço')),
                ('enderecoNumero', models.CharField(blank=True, max_length=8, verbose_name='Nº Endereço')),
                ('enderecoComplemento', models.CharField(blank=True, max_length=30, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=40)),
                ('cidade', models.CharField(blank=True, default='Teresina', max_length=50)),
                ('estado', models.CharField(blank=True, default='PI', max_length=2)),
                ('CEP', models.CharField(blank=True, max_length=10)),
                ('observacao', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observação')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('pergunta', models.TextField(blank=True, max_length=50, null=True, verbose_name='Pergunta')),
                ('ativo', models.BooleanField(default=True)),
                ('CadastradoPor', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_cadastrado_por', to=settings.AUTH_USER_MODEL, verbose_name='Cadastrado Por')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
