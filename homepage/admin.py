from django.contrib import admin
from homepage.models import Activity


# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']
    search_fields = ['title', 'description']
    ordering = ['created']