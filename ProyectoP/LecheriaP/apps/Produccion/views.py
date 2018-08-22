# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.Produccion.forms import ProduccionForm

from apps.Produccion.models import Registro_Produccion

# Create your views here.

def index(request):
	return render(request, 'Produccion/index.html')


def Produccion_view(request):
	if request.method == 'POST':
		form = ProduccionForm(request.POST)
		if form.is_valid():
			form.save()
	 	return redirect('Produccion:index')
	else:
		form = ProduccionForm()
	return render(request, 'Produccion/Produccion_form.html', {'form':form})

def Produccion_list(request):
	produccion = Registro_Produccion.objects.all().order_by('id')
	contexto = {'Produccion':produccion}
	return render(request, 'Produccion/Produccion_list.html', contexto)

def Produccion_edit(request, id_Produccion):
	produccion = Registro_Produccion.objects.get(id=id_Produccion)
	if request.method == 'GET':
		form = ProduccionForm(instance=produccion)
	else:
		form = ProduccionForm(request.POST, instance=produccion)
		if form.is_valid():
			form.save()
		return redirect('Produccion:Produccion_listas')
	return render(request, 'Produccion/Produccion_form.html', {'form':form})

def Produccion_delete(request, id_Produccion):
	produccion = Registro_Produccion.objects.get(id=id_Produccion)
	if request.method == 'POST':
		produccion.delete()
		return redirect('Produccion:Produccion_listas')
	return render(request, 'Produccion/Produccion_delete.html', {'Produccion':produccion}) 