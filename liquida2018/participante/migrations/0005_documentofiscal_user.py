# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('participante', '0004_auto_20180608_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentofiscal',
            name='user',
            field=models.ForeignKey(default='1', to=settings.AUTH_USER_MODEL),
        ),
    ]
