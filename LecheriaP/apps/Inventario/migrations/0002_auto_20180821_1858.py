# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-22 00:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad_carretillos',
            new_name='cantidad_de_carretillos',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad_desparasitantes',
            new_name='cantidad_de_desparasitantes',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad_estanon_miel',
            new_name='cantidad_de_estanones_con_miel',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad_ordenadoras',
            new_name='cantidad_de_ordenadoras',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad_pacas',
            new_name='cantidad_de_pacas',
        ),
        migrations.RenameField(
            model_name='inventario',
            old_name='cantidad_palas',
            new_name='cantidad_de_palas',
        ),
    ]
