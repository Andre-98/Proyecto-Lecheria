# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.Reportes.forms import ReportesForm

from apps.Reportes.models import Reportes

# Create your views here.

def index(request):
	return render(request, 'Reportes/index.html')


def Reportes_view(request):
	if request.method == 'POST':
		form = ReportesForm(request.POST)
		if form.is_valid():
			form.save()
	 	return redirect('Reportes:index')
	else:
		form = ReportesForm()
	return render(request, 'Reportes/Reportes_form.html', {'form':form})

def Reportes_list(request):
	reportes = Reportes.objects.all().order_by('id')
	contexto = {'Reportes':reportes}
	return render(request, 'Reportes/Reportes_list.html', contexto)

def Reportes_edit(request, id_Reportes):
	reportes = Reportes.objects.get(id=id_Reportes)
	if request.method == 'GET':
		form = ReportesForm(instance=reportes)
	else:
		form = ReportesForm(request.POST, instance=reportes)
		if form.is_valid():
			form.save()
		return redirect('Reportes:Reportes_listas')
	return render(request, 'Reportes/Reportes_form.html', {'form':form})

def Reportes_delete(request, id_Reportes):
	reportes = Reportes.objects.get(id=id_Reportes)
	if request.method == 'POST':
		reportes.delete()
		return redirect('Reportes:Reportes_listas')
	return render(request, 'Reportes/Reportes_delete.html', {'Reportes':reportes})