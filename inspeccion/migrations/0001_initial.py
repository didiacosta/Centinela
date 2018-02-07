# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaInicio', models.DateTimeField(auto_now=True)),
                ('longitud', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=50)),
                ('fechaTerminacion', models.DateTimeField()),
                ('observacion', models.CharField(max_length=255)),
                ('programacion', models.ForeignKey(related_name=b'inspeccion_programacion', on_delete=django.db.models.deletion.PROTECT, to='programacion.Programacion')),
            ],
            options={
                'permissions': (('can_see_inspeccion', 'can see inspeccion'),),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='inspeccion',
            unique_together=set([('programacion', 'fechaInicio')]),
        ),
    ]
