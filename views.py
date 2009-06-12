from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template
from constants import home

def index(request):
    return direct_to_template(request, "index.html")

def about(request):
    return direct_to_template(request, "about.html", {
       'breadcrumb': [ home, { 'title': "About" } ] 
    })

def sandbox(request):
    return direct_to_template(request, "sandbox.html")
