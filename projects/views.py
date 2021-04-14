from django.shortcuts import render
from .models import Project


def project(request):

    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})
