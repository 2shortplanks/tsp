from django.conf.urls.defaults import *

urlpatterns = patterns('tsp.projects.views',
    (r'^$', 'index'),
    (r'^section/(?P<fragment>.+)/$', 'section_detail'),
    (r'^(?P<fragment>.+)/$', 'project_detail'),
)