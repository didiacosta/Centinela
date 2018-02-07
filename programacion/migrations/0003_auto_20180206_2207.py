# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0002_programacion_abierta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programacion',
            name='abierta',
        ),
        migrations.AddField(
            model_name='programacion',
            name='cerrada',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
