# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.db import models

# Create your models here.
class Inventario(models.Model):
	cantidad_de_pacas = models.IntegerField()
	cantidad_de_carretillos = models.IntegerField()
	cantidad_de_palas = models.IntegerField()
	cantidad_de_desparasitantes = models.IntegerField()
	cantidad_de_ordenadoras = models.IntegerField() 
	cantidad_de_estanones_con_miel = models.IntegerField()