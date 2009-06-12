from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template
from django.shortcuts import get_object_or_404

from projects.models import *
from django.core.exceptions import ObjectDoesNotExist

from constants import home

def index(request):
    return direct_to_template(request, "projects.html", {
       'breadcrumb': [ home, { 'title': "Projects" } ] 
    })

def section_detail(request, fragment):
    ps = get_object_or_404(ProjectSection,slug=fragment)
    return direct_to_template(request, "projects_category_detail.html", {
       'breadcrumb': [ home, {}, { 'title': ps.name } ] 
    })

def project_detail(request, fragment):
    proj = get_object_or_404(Project,slug=fragment)
    return direct_to_template(request, "projects_project_detail.html", {
       'breadcrumb': [ home, {}, { 'title': proj.name } ] 
    })


