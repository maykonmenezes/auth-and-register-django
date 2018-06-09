# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0005_documentofiscal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='photo',
            field=models.ImageField(blank=True, upload_to='docs/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='documentofiscal',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
