# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0002_auto_20180606_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='CPF',
        ),
    ]
