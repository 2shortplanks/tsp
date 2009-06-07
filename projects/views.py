from django.http import HttpResponse

from chouwa.shortcuts import direct_to_template


def index(request):
    return direct_to_template(request, "foo")

def detail(request, project_tag):
    return HttpResponse("detail")

