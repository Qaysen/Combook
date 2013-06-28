from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from app.views import EntryListView,EntryCreateView

admin.autodiscover()

urlpatterns = patterns('',

	url(r'Crear/',EntryCreateView.as_view(),name='Crear'),
	url(r'Libro/',EntryListView.as_view(),name='Libro'),
	
	url(r'^$','app.views.inicio'),

	url(r'^buscar_libros/','app.views.buscar_libros'),

	url(r'^libros/', 'app.views.libro_Registro'),

	url(r'^buscar/', 'app.views.busqueda'),
	
	url(r'^registrar_libro','app.views.registrar_libro'),

	url(r'^mostrar_libro/','app.views.mostrar_libro'),

 
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

)
