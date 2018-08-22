# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.db import models

# Create your models here.


class Reportes(models.Model):
	Dia = 'Día'
	Semana = 'Semana'
	Mes = 'Mes'
	Ano = 'Año'

	Produccion_lactea_grupal = (
		(Dia, 'Día'),
		(Semana, 'Semana'),
		(Mes, 'Mes'),
		(Ano, 'Año'),
	)
	produccion_lactea_grupal_por = models.CharField(
		max_length = 10,
		choices = Produccion_lactea_grupal, 
		default = Dia,
	)
	def is_upperclass(self):
		return self.produccion_lactea_grupal in (self.Dia, self.Semana, self.Mes, self.Ano)
	
	lista_de_vacas_prenadas = models.IntegerField(null=True)
	lista_de_vacas_en_produccion = models.IntegerField(null=True)
	lista_de_toros = models.IntegerField(null=True)
	lista_de_novillas = models.IntegerField(null=True)
	lista_de_novillos = models.IntegerField(null=True)
	lista_de_terneras = models.IntegerField(null=True)
	lista_de_terneros = models.IntegerField(null=True)
