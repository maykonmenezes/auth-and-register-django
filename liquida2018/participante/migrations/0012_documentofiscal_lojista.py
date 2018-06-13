# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojista', '0002_auto_20180610_1122'),
        ('participante', '0011_auto_20180609_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentofiscal',
            name='lojista',
            field=models.ForeignKey(default=1, related_name='rel_lojista', to='lojista.Lojista'),
        ),
    ]
