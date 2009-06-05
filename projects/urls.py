from django.conf.urls.defaults import *

urlpatterns = patterns('tsp.projects.views',
    (r'^$', 'index'),
    (r'^(?P<project_tag>\d+)/$', 'detail'),
)