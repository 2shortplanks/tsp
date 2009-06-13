from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template
from django.shortcuts import get_object_or_404

from projects.models import *
from django.core.exceptions import ObjectDoesNotExist

from django.core.urlresolvers import reverse

from constants import home

def index(request):
    return direct_to_template(request, "projects/index.html", {
       'breadcrumb': [ home, { 'title': "Projects" } ] 
    })

def breadcrumb_for_project_section(section):
    if section.parent:
        result = breadcrumb_for_project_section(section.parent)
    else:
        result = [ home ]
    result.append({ 'title': section.name, 'link': reverse("projects_section_detail", kwargs={ 'slug': section.slug }) })
    return result

def section_detail(request, slug):
    ps = get_object_or_404(ProjectSection,slug=slug)
    return direct_to_template(request, "projects/category_detail.html", {
       'breadcrumb': breadcrumb_for_project_section(ps),
       'section': ps
    })

def breadcrumb_for_project(project):
    ps = project.section
    breadcrumb = breadcrumb_for_project_section(ps)
    breadcrumb.append({ 'title': project.name, 'link': reverse("projects_section_detail", kwargs={ 'slug': ps.slug }) })
    return breadcrumb

def project_detail(request, slug):
    proj = get_object_or_404(Project,slug=slug)
    return direct_to_template(request, "projects/project_detail.html", {
       'breadcrumb': breadcrumb_for_project(proj),
       'project': proj
    })


