# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0008_auto_20180608_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentofiscal',
            name='user',
            field=models.ForeignKey(to='participante.Profile'),
        ),
    ]
