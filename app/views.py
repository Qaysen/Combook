from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import RegLibroForm
from app.models import *
#USANDO CLASES!! ---------------------------------------------------------
from django.views.generic import ListView,CreateView,UpdateView,DetailView

class LibroUpdateView(UpdateView):
	model=Libro

class LibroDetailView(DetailView):
	model = Libro

#crear libro
class LibroCreateView(CreateView):
	model=Libro
#listar libros
class LibroListView(ListView):
	"""docstring for EntryListView"""
	model= Libro
	template_name='app/libro_list.html' #ubicacion por defecto(puedes cambiarla)
	context_object_name='libro_list'
#--------------------------------------------------------------------------
def libro_Registro(request):
	libros = Libro.objects.all()
	dic = {"libros":libros}
	return render_to_response('libros.html',dic,context_instance=RequestContext(request))

def inicio (request):
	return render_to_response('inicio.html','base.html',context_instance=RequestContext(request))
	
def buscar_libros (request):
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
		formulario = RegLibroForm(request.POST)

		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/libros')
	else:
		formulario = RegLibroForm()
	return render_to_response('registrar_libro.html',{'formulario':formulario},context_instance=RequestContext(request))
 