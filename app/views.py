from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import *

def libro_Registro(request):
	libros = Libro.objects.all()
	dic = {"libros":libros}
	return render_to_response('libros.html',dic,context_instance=RequestContext(request))

def inicio (request):
	return render_to_response('base.html',context_instance=RequestContext(request))