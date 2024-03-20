from django.urls import path
from projects.views import projects
from .views import project_detail

app_name = 'projects'

urlpatterns = [
    path('', projects, name='projects'),
    path('<int:project_id>/', project_detail, name='project_detail'),
]
