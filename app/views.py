from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import RegLibroForm
from app.models import *

def libro_Registro(request):
	libros = Libro.objects.all()
	dic = {"libros":libros}
	return render_to_response('libros.html',dic,context_instance=RequestContext(request))

def inicio (request):
	return render_to_response('base.html',context_instance=RequestContext(request))

def inicio (request):
	return render_to_response('buscar_libros.html',context_instance=RequestContext(request))

def registrar_libro(request):
	if request.method=='POST':
		formulario = RegLibroForm(request.POST,request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/libros')
	else:
		formulario = RegLibroForm()
	return render_to_response('registrar_libro.html',{'formulario':formulario},context_instance=RequestContext(request))
 