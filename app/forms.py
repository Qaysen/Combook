#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import *

class RegLibroForm(ModelForm):
	
	class Meta:
		model=Libro