# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reportes', '0003_auto_20180821_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportes',
            name='listado_novillas',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='listado_novillos',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='listado_terneras',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='listado_terneros',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='listado_toros',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='listado_vacas_en_produccion',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reportes',
            name='listado_vacas_prenadas',
            field=models.IntegerField(null=True),
        ),
    ]