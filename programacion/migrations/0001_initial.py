# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(related_name=b'departamento_municipio', on_delete=django.db.models.deletion.PROTECT, to='programacion.Departamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('ordenServicio', models.CharField(max_length=25)),
                ('nombreProyecto', models.CharField(max_length=255)),
                ('inspector', models.ForeignKey(related_name=b'programacion_usuario', on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario')),
                ('municipio', models.ForeignKey(related_name=b'programacion_municipio', on_delete=django.db.models.deletion.PROTECT, to='programacion.Municipio')),
            ],
            options={
                'permissions': (('can_see_programacion', 'can see programacion'),),
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='programacion',
            unique_together=set([('inspector', 'fecha')]),
        ),
    ]
