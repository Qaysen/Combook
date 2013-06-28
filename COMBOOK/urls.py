from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from app.views import EntryCreateView,EntryListView,EntryUpdateView
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'^$','app.views.inicio'),
	url(r'^buscar/','app.views.buscar_libros'),
	url(r'^registrar_categoria/','app.views.registrar_categoria'),

	url(r'^libros/', 'app.views.libro_Registro'),
	url(r'^listar/',EntryListView.as_view(), name= 'entry_list'),
	url(r'^create/',EntryCreateView.as_view(), name= 'create_libro'),
	url(r'^update/(?P<pk>\d+)$',EntryUpdateView.as_view(), name= 'entry_update'),

	url(r'^buscar/', 'app.views.busqueda'),
	
	url(r'^registrar_libro/','app.views.registrar_libro'),
 
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

)
