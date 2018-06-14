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
        ('participante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCupom', models.CharField(max_length=12, unique=True, verbose_name='Número do Cupom')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em')),
                ('impresso', models.BooleanField(default=False)),
                ('dataImpressao', models.DateTimeField()),
                ('documentoFiscal', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='rel_cupom_doc', to='participante.DocumentoFiscal')),
                ('operador', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_cupom_operador', to=settings.AUTH_USER_MODEL, verbose_name='Cadastrado Por')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='rel_cupom_participante', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
