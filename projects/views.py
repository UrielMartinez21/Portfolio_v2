from django.shortcuts import render
from projects.models import Project


# Create your views here.
def projects(request):
    # Obtener todos los proyectos
    all_projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': all_projects})


def project_detail(request, project_id):
    # Get project by ID
    project = Project.objects.get(id=project_id)
    # Get explanations
    explanations = project.explanation.split('\n')
    # Add explanations to project
    project.explanation = explanations
    return render(request, 'projects/project_detail.html', {'project': project})
