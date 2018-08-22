from __future__ import unicode_literals

from __future__ import absolute_import

from django import forms

from apps.Reportes.models import Reportes


class ReportesForm(forms.ModelForm):

	class Meta:
		model = Reportes

		fields = [
			'produccion_lactea_grupal_por',
			'lista_de_vacas_prenadas',
			'lista_de_vacas_en_produccion',
			'lista_de_toros',
			'lista_de_novillas',
			'lista_de_novillos',
			'lista_de_terneras',
			'lista_de_terneros',
		]
		labels = {
			'produccion_lactea_grupal_por': 'Produccion Lactea Grupal por',
			'lista_de_vacas_prenadas': 'Lista de Vacas Prenadas',
			'lista_de_vacas_en_produccion': 'Lista de Vacas Produciendo',
			'lista_de_toros': 'Lista de Toros',
			'lista_de_novillas': 'Lista de Novillas',
			'lista_de_novillos': 'Lista de Novillos',
			'lista_de_terneras': 'Lista de Terneras',
			'lista_de_terneros': 'Lista de Terneros',
		}
		widgets = {
			'produccion_lactea_grupal_por': forms.Select(attrs={'class': 'form-control'}),
			'lista_de_vacas_prenadas': forms.TextInput(attrs={'class': 'form-control'}),
			'lista_de_vacas_en_produccion': forms.TextInput(attrs={'class': 'form-control'}),
			'lista_de_toros': forms.TextInput(attrs={'class': 'form-control'}),
			'lista_de_novillas': forms.TextInput(attrs={'class': 'form-control'}),
			'lista_de_novillos': forms.TextInput(attrs={'class': 'form-control'}),
			'lista_de_terneras': forms.TextInput(attrs={'class': 'form-control'}),
			'lista_de_terneros': forms.TextInput(attrs={'class': 'form-control'}),
		}