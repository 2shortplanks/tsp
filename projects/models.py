from django.db import models

from constants import *
from django.core.urlresolvers import reverse

class ProjectSection(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = models.ForeignKey('ProjectSection', null=True, blank=True)
    def __unicode__(self):
        return self.name
    def breadcrumb(self):
        if self.parent:
            result = self.parent.breadcrumb()
        else:
            result = [ home ]
        result.append({ 'title': self.name, 'link': reverse("projects_section_detail", kwargs={ 'slug': self.slug }) })
        return result

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    synopsis = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    section = models.ForeignKey(ProjectSection)
    def __unicode__(self):
        return self.name