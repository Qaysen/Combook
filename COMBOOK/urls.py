from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$','app.views.inicio'),

	url(r'^libros/', 'app.views.libro_Registro'),
 
   	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

  	url(r'^admin/', include(admin.site.urls)),

)
