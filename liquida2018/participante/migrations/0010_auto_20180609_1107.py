# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0009_auto_20180608_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='user',
            field=models.ForeignKey(related_name='rel_username', to=settings.AUTH_USER_MODEL),
        ),
    ]
