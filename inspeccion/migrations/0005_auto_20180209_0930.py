# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspeccion', '0004_auto_20180208_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='latitud',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inspeccion',
            name='longitud',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
