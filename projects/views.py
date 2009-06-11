from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template

from projects.models import *
from django.core.exceptions import ObjectDoesNotExist

from constants import home

def index(request):
    return direct_to_template(request, "projects.html", {
       'breadcrumb': [ home, { 'title': "Projects" } ] 
    })

# there has to be a better way to write this at a url level
def detail(request, fragment="foo"):
    try:
        ps = ProjectSection.objects.get(slug=fragment)
        return direct_to_template(request, "projects_category_detail.html", {
           'breadcrumb': [ home, {}, { 'title': ps.name } ] 
        })
    except ObjectDoesNotExist:
        ps = Project.objects.get(slug=fragment)
        return direct_to_template(request, "projects_project_detail.html", {
           'breadcrumb': [ home, {}, { 'title': ps.name } ] 
        })


