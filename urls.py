from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover();

# some of the more basic pages just go straight to a template
from django.views.generic.simple import *

urlpatterns = patterns('',
    # Example:
    # (r'^tsp/', include('tsp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    # the homepage and other simple pages
    (r'^$', direct_to_template, { 'template': 'index.html' }),
    (r'^about', direct_to_template, { 'template': 'about.html' }),
)
