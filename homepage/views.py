from django.shortcuts import render

from homepage.models import Activity, Description


def home(request):
    # Get all activities
    all_activities = Activity.objects.all()
    return render(request, 'home.html', {'activities': all_activities})


def about_me(request):
    # Get information per type
    personal = Description.objects.filter(type='personal')
    education = Description.objects.filter(type='education')
    jobs = Description.objects.filter(type='jobs')
    skills = Description.objects.filter(type='skills')
    career = Description.objects.filter(type='career')

    # Create a dictionary with all the information
    info = {
        'educations': education,
        'jobs': jobs,
        'careers': career,
        'skills': skills,
        'personals': personal,
    }

    return render(request, 'about_me.html', info)
