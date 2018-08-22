# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.Inventario.forms import InventarioForm

from apps.Inventario.models import Inventario

# Create your views here.

def index(request):
	return render(request, 'Inventario/index.html')


def Inventario_view(request):
	if request.method == 'POST':
		form = InventarioForm(request.POST)
		if form.is_valid():
			form.save()
	 	return redirect('Inventario:index')
	else:
		form = InventarioForm()
	return render(request, 'Inventario/Inventario_form.html', {'form':form})

def Inventario_list(request):
	inventario = Inventario.objects.all().order_by('id')
	contexto = {'Inventario':inventario}
	return render(request, 'Inventario/Inventario_list.html', contexto)

def Inventario_edit(request, id_Inventario):
	inventario = Inventario.objects.get(id=id_Inventario)
	if request.method == 'GET':
		form = InventarioForm(instance=inventario)
	else:
		form = InventarioForm(request.POST, instance=inventario)
		if form.is_valid():
			form.save()
		return redirect('Inventario:Inventario_listas')
	return render(request, 'Inventario/Inventario_form.html', {'form':form})

def Inventario_delete(request, id_Inventario):
	inventario = Inventario.objects.get(id=id_Inventario)
	if request.method == 'POST':
		inventario.delete()
		return redirect('Inventario:Inventario_listas')
	return render(request, 'Inventario/Inventario_delete.html', {'Inventario':inventario})