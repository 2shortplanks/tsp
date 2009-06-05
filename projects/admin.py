from tsp.projects.models import *
from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

class ProjectSectionAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("name",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectSection, ProjectSectionAdmin)
