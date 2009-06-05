from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    pub_date = models.DateTimeField('date published')
