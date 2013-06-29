from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from app.views import EntryCreateView,EntryListView,EntryUpdateView
from app.views import EntryListView,EntryCreateView
from app.views import LibroListView,LibroCreateView,LibroUpdateView,LibroDetailView

admin.autodiscover()

urlpatterns = patterns('',

	url(r'Crear/',EntryCreateView.as_view(),name='Crear'),
	url(r'Libro/',EntryListView.as_view(),name='Libro'),
	
	url(r'^$','app.views.inicio'),
	url(r'^buscar/','app.views.buscar_libros'),
	url(r'^registrar_categoria/','app.views.registrar_categoria'),
	url(r'^plantilla_libro/','app.views.plantilla_libro'),
	url(r'^buscar_libros/','app.views.buscar_libros'),

	# USANDO CLASES!-------------------------------------------------
	url(r'^update/(?P<pk>\d+)$',LibroUpdateView.as_view(),name='libro_update'),

	url(r'^libro/(?P<pk>\d+)$',LibroDetailView.as_view(),name='libro_detail'),

	url(r'^$','app.views.buscar_libros'),
	#la clase hecha en views, la hacemos pasar como 
	url(r'^listar/',LibroListView.as_view(),name='libro_list'),

	url(r'^crear/',LibroCreateView.as_view(),name='libro_create'),

	url(r'^$','app.views.inicio'),
	#---------------------------------------------------------------
	url(r'^libros/', 'app.views.libro_Registro'),
	url(r'^listar/',EntryListView.as_view(), name= 'entry_list'),
	url(r'^create/',EntryCreateView.as_view(), name= 'create_libro'),
	url(r'^update/(?P<pk>\d+)$',EntryUpdateView.as_view(), name= 'entry_update'),

	url(r'^buscar/', 'app.views.busqueda'),
	url(r'^registrar_libro/','app.views.registrar_libro'),
	url(r'^registrar_libro','app.views.registrar_libro'),
	url(r'^mostrar_libro/','app.views.mostrar_libro'),
	url(r'^registrar_libro/','app.views.registrar_libro'),
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
