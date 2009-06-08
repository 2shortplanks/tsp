from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template

from constants import home

def index(request):
    return direct_to_template(request, "projects.html", {
       'breadcrumb': [ home, { 'title': "Projects" } ] 
    })
def detail(request, project_tag):
    return HttpResponse("detail")

