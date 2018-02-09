# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspeccion', '0003_auto_20180208_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='observacion',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
