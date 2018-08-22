# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import

from django.shortcuts import render, redirect

from django.http import HttpResponse

from apps.Animal.forms import AnimalForm

from apps.Animal.models import Animal

# Create your views here.

def index(request):
	return render(request, 'Animal/index.html')


def Animal_view(request):
	if request.method == 'POST':
		form = AnimalForm(request.POST)
		if form.is_valid():
			form.save()
	 	return redirect('Animal:index')
	else:
		form = AnimalForm()
	return render(request, 'Animal/Animal_form.html', {'form':form})

def Animal_list(request):
	animal = Animal.objects.all().order_by('id')
	contexto = {'Animal':animal}
	return render(request, 'Animal/Animal_list.html', contexto)

def Animal_edit(request, id_Animal):
	animal = Animal.objects.get(id=id_Animal)
	if request.method == 'GET':
		form = AnimalForm(instance=animal)
	else:
		form = AnimalForm(request.POST, instance=animal)
		if form.is_valid():
			form.save()
		return redirect('Animal:Animal_listas')
	return render(request, 'Animal/Animal_form.html', {'form':form})

def Animal_delete(request, id_Animal):
	animal = Animal.objects.get(id=id_Animal)
	if request.method == 'POST':
		animal.delete()
		return redirect('Animal:Animal_listas')
	return render(request, 'Animal/Animal_delete.html', {'Animal':animal}) 
