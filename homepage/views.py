from django.shortcuts import render

from homepage.models import Activity
from projects.models import Project


def home(request):
    # Get all activities
    all_activities = Activity.objects.all()
    return render(request, 'home.html', {'activities': all_activities})


def about_me(request):
    return render(request, 'about_me.html')


def projects(request):
    # Obtener todos los proyectos
    all_projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': all_projects})
