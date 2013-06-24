from django.db import models

class Alumno(models.Model):
	nombre             = models.CharField(max_length=200)
	apellido           = models.CharField(max_length=10)
	dni                = models.CharField(max_length=8)
	fecha_nac          = models.DateField()
	def __unicode__(self):
		return "%s  %s"%(self.nombre,self.apellido)
		
class Libro(models.Model):
	"""docstring for libro"""
	codigo             = models.CharField(max_length=200)
	titulo             = models.CharField(max_length=200)
	editorial          = models.CharField(max_length=200)
	fecha_publicacion  = models.CharField(max_length=20)
	def __unicode__(self):
		return "%s "%(self.titulo)
		
class Autor(models.Model):
	"""docstring for libro"""
	codigo             = models.CharField(max_length=200)
	nombre             = models.CharField(max_length=200)
	apellido           = models.CharField(max_length=200)
	bibliografia       = models.CharField(max_length=200)
	def __unicode__(self):
		return "%s "%(self.nombre)

class Escribir(models.Model):
	# requerido
	fk_codigo_libro    = models.ForeignKey(Libro)
	fk_codigo_autor    = models.ForeignKey(Autor)
	fk_codigo_escribir = models.CharField(max_length=200)
	def __unicode__(self):
		return "esc %s atr %s lbr %s "%(fk_codigo_escribir,fk_codigo_autor,fk_codigo_libro)