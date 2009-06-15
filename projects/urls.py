from django.conf.urls.defaults import *

urlpatterns = patterns('tsp.projects.views',
    (r'^$', 'index', {}, "projects_index"),
    (r'^section/(?P<slug>.+)/$', 'section_detail', {}, "projects_section_detail"),
    (r'^(?P<slug>.+)/$', 'project_detail', {}, "projects_project_detail"),
)