from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template
from django.shortcuts import get_object_or_404

from projects.models import *
from django.core.exceptions import ObjectDoesNotExist

from constants import home

def index(request):
    return direct_to_template(request, "projects/index.html", {
       'breadcrumb': [ home, { 'title': "Projects" } ] 
    })

def section_detail(request, fragment):
    ps = get_object_or_404(ProjectSection,slug=fragment)
    return direct_to_template(request, "projects/category_detail.html", {
       'breadcrumb': [ home, {}, { 'title': ps.name } ],
       'section': ps
    })

def project_detail(request, fragment):
    proj = get_object_or_404(Project,slug=fragment)
    return direct_to_template(request, "projects/project_detail.html", {
       'breadcrumb': [ home, {}, { 'title': proj.name } ] 
    })


