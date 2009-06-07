from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover();

import os

# some of the more basic pages just go straight to a template
from django.views.generic.simple import *

from views import *

urlpatterns = patterns('',
    # Example:
    # (r'^tsp/', include('tsp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    
    # the homepage and other simple pages
    (r'^$', index),
    (r'^about/$', about),
    
    # the various subprojects
    (r'projects/', include('tsp.projects.urls')),
    
    # static file serving.  This is bad, and wrong, but in production this entire url path
    # will not be proxied by the webserver, so it doesn't matter
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\','/')}),
)
