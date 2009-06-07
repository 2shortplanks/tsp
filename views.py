from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template

def index(request):
    return direct_to_template(request, "index.html")

def about(request):
    return direct_to_template(request, "about.html")

