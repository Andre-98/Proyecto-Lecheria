# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animal', '0002_auto_20180820_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='fecha_aproximada_parto',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='fecha_aumento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='cantidad_partos',
            field=models.IntegerField(null=True),
        ),
    ]