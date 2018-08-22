from __future__ import unicode_literals

from __future__ import absolute_import

from django import forms

from apps.Produccion.models import Registro_Produccion


class ProduccionForm(forms.ModelForm):

	class Meta:
		model = Registro_Produccion

		fields = [
			'produccion_diaria',
			'Animales',
			'fecha_de_produccion',
			'cantidad_producida',
			'unidad_de_medida',
		]
		labels = {
			'produccion_diaria': 'Produccion Diaria',
			'Animales': 'Animales',
			'fecha_produccion': 'Fecha de Produccion',
			'cantidad_producida': 'Cantidad Producida',
			'unidad_de_medida': 'Unidad de Medida',
		}
		widgets = {
			'produccion_diaria': forms.Select(attrs={'class': 'form-control'}),
			'Animales': forms.CheckboxSelectMultiple(),
			'fecha_produccion': forms.TextInput(attrs={'class': 'form-control'}),
			'cantidad_producida': forms.TextInput(attrs={'class': 'form-control'}),
			'unidad_de_medida': forms.Select(attrs={'class': 'form-control'}),		
		}