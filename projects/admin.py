from django.contrib import admin
from projects.models import Project


# Register your models here.
# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description']
    ordering = ['created']