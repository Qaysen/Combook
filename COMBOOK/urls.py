from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','app.views.inicio'),
	url(r'^$','app.views.buscar_libros'),

	url(r'^libros/', 'app.views.libro_Registro'),

	url(r'^buscar/', 'app.views.busqueda'),
	
	url(r'^registrar_libro','app.views.registrar_libro'),
 
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),
  	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

)
