from __future__ import unicode_literals

from __future__ import absolute_import

from django import forms

from apps.Inventario.models import Inventario


class InventarioForm(forms.ModelForm):

	class Meta:
		model = Inventario

		fields = [
			'cantidad_de_pacas',
			'cantidad_de_carretillos',
			'cantidad_de_palas',
			'cantidad_de_desparasitantes',
			'cantidad_de_ordenadoras',
			'cantidad_de_estanones_con_miel',
		]
		labels = {
			'cantidad_de_pacas': 'Cantidad de Pacas',
			'cantidad_de_carretillos': 'Cantidad de Carretillos',
			'cantidad_de_palas': 'Cantidad de Palas',
			'cantidad_de_desparasitantes': 'Cantidad de Desparasitantes',
			'cantidad_de_ordenadoras': 'Cantidad de Ordenadoras',
			'cantidad_de_estanones_con_miel': 'Cantidad de Estanones con Miel',
		}
		widgets = {
			'cantidad_de_pacas': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_de_carretillos': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_de_palas': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_de_desparasitantes': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_de_ordenadoras': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_de_estanon_miel': forms.TextInput(attrs={'class': 'form-control'}),	
		}