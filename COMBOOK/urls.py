from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from app.views import EntryListView,EntryCreateView,EntryUpdateView,EntryDetailView,EntryCreateViewLibro

admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$','app.views.inicio'),

	url(r'^$','app.views.inicio'),
	## vistas  con clases 
	url(r'^listar/',EntryListView.as_view(),name="listar"),

	url(r'^Iingresar/',EntryCreateView.as_view(),name="crear"),

	url(r'^nuevolibro/',EntryCreateViewLibro.as_view(),name="nuevoLibro"),

	url(r'^modificar/(?P<pk>\d+)$',EntryUpdateView.as_view(),name="modificar"),

	url(r'^mod/(?P<pk>\d+)$',EntryDetailView.as_view(),name="Detalle_modificar"),
	## vistas  con clases 
	url(r'^libros/', 'app.views.libro_Registro'),

	url(r'^buscar/', 'app.views.busqueda'),
	
	url(r'^registrar_libro','app.views.registrar_libro'),
 
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

)
