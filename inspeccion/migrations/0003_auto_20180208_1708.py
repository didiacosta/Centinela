# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspeccion', '0002_remove_inspeccion_fechaterminacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='observacion',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
