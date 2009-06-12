from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template

from projects.models import *
from django.core.exceptions import ObjectDoesNotExist

from constants import home

def index(request):
    return direct_to_template(request, "projects.html", {
       'breadcrumb': [ home, { 'title': "Projects" } ] 
    })

def section_detail(request, fragment):
    ps = ProjectSection.objects.get(slug=fragment)
    return direct_to_template(request, "projects_category_detail.html", {
       'breadcrumb': [ home, {}, { 'title': ps.name } ] 
    })

def project_detail(request, fragment):
    ps = Project.objects.get(slug=fragment)
    return direct_to_template(request, "projects_project_detail.html", {
       'breadcrumb': [ home, {}, { 'title': ps.name } ] 
    })


