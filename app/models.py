# encoding:utf-8
from django.db import models
from django.core.urlresolvers import reverse


IDIOMA = (
    ('ES', 'Español'),
    ('EN', 'Ingles'),
    ('AL', 'Aleman'),
    ('PO', 'Portugues'),
    ('TR', 'Turco'),
    ('UK', 'Ucraniano'),
    ('RU', 'Ruso'),
    ('JA', 'Japones'),
)


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=60)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=20)
    fecha_nac = models.DateField()

    def __unicode__(self):
        return "%s  %s" % (self.nombre, self.apellido)


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    seudonimo = models.CharField(max_length=60, null=True, blank=True)
    pais = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=5000, null=True, blank=True)
    foto = models.ImageField(upload_to='foto_autor')

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Detalle_modificar", kwargs={'pk': self.id})


class Editorial(models.Model):

    nombre = models.CharField(max_length=100)
    propietario = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    idioma = models.CharField(max_length=30, choices=IDIOMA)
    portada = models.ImageField(upload_to='portadas/')
    numero_edicion = models.IntegerField(max_length=10)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial)

    def __str__(self):
        return self.titulo


class Tema(models.Model):
    libro = models.ForeignKey(Libro)
    texto = models.CharField(max_length=40)

    def __str__(self):
        return self.texto
