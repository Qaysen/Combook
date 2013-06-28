from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import RegLibroForm
from django.views.generic import CreateView,ListView
from app.models import *


class EntryCreateView(CreateView):
	model=Libro
	template_name="libro_form.html"

class EntryListView(ListView):
	model=Libro
	template_name="libro_list.html"
	context_object_name="entry_list"


def libro_Registro(request):
	libros = Libro.objects.all()
	dic = {"libros":libros}
	return render_to_response('libros.html',dic,context_instance=RequestContext(request))

def inicio (request):
	return render_to_response('inicio.html',context_instance=RequestContext(request))
	

def buscar_libros(request):
	return render_to_response('buscar_libros.html',context_instance=RequestContext(request))

def busqueda(request):
	if request.method == "POST":
		buscar = request.POST["busca_palabra"]
		libros = Libro.objects.filter(titulo__icontains=buscar)
		return render_to_response(
			'busqueda.html',
			{'libros':libros},
			context_instance=RequestContext(request)
		)

def registrar_libro(request):
	if request.method=='POST':
		print request.POST
		for i in request.POST.items():
			print i
		formulario = RegLibroForm(request.POST,request.FILES)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/libros')
	else:
		formulario = RegLibroForm()
	return render_to_response('registrar_libro.html',{'formulario':formulario},context_instance=RequestContext(request))

def mostrar_libro(request):
	return render_to_response('mostrar_libro.html',context_instance=RequestContext(request))

 