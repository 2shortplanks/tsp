from django.db import models

class ProjectSection(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = models.ForeignKey('ProjectSection', null=True, blank=True)

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    synopsis = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    section = models.ForeignKey(ProjectSection)

