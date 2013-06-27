#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import Libro

class RegLibroForm(ModelForm):
	#codigo = forms.RegexField(max_length=15, regex=r'^[a-zA-Z0-9 ]+$', help_text = "Ingrese codigo", error_message = "Solo caracteres alfanumericos.")
	#titulo = forms.RegexField(max_length=50, regex=r'^[a-zA-Z0-9 ]+$', help_text = "Ingrese titulo", error_message = "Solo caracteres alfanumericos.")
	#editorial = forms.RegexField(max_length=50, regex=r'^[a-zA-Z0-9 ]+$', help_text = "Ingrese editorial", error_message = "Solo caracteres alfanumericos.")
	#fecha_publicacion = forms.DateField()
	#portada = models.ImageField(upload_to='portadas',verbose_name='Imagen')
	class Meta:
		model=Libro