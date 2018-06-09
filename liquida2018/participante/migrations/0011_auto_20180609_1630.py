# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0010_auto_20180609_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='user',
            field=models.ForeignKey(editable=False, related_name='rel_username', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pergunta',
            field=models.TextField(verbose_name='Pergunta', max_length=50, blank=True, null=True),
        ),
    ]
