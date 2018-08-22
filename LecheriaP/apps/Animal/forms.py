from __future__ import unicode_literals

from __future__ import absolute_import

from django import forms

from apps.Animal.models import Animal


class AnimalForm(forms.ModelForm):

	class Meta:
		model = Animal

		fields = [
			'identificacion_numerica',
			'nombre',
			'sexo', 
			'fecha_de_nacimiento', 
			'edad',  
			'raza', 
			'foto', 
			'etapa_del_animal',
			'estado_del_animal',
			'cantidad_de_partos',
		]
		labels = {
			'identificacion_numerica': 'Identificacion Numerica',
			'nombre': 'Nombre',
			'sexo': 'Sexo', 
			'fecha_nacimiento': 'Fecha Nacimiento', 
			'edad': 'Edad',  
			'raza': 'Raza', 
			'foto': 'Foto',	
			'etapa': 'Etapa',
			'estado': 'Estado', 
			'cantidad_partos': 'Cantidad de Partos',
		}
		widgets = {
			'identificacion_numerica': forms.TextInput(attrs={'class': 'form-control'}),
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'sexo': forms.TextInput(attrs={'class': 'form-control'}), 
			'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}), 
			'edad': forms.TextInput(attrs={'class': 'form-control'}),  
			'raza': forms.TextInput(attrs={'class': 'form-control'}), 
			'foto': forms.TextInput(attrs={'class': 'form-control'}),
			'etapa': forms.Select(attrs={'class': 'form-control'}),
			'estado': forms.Select(attrs={'class': 'form-control'}),
			'cantidad_partos': forms.TextInput(attrs={'class': 'form-control'}),		
		}