from django.shortcuts import render, get_object_or_404
from .models import Project, Experience, Profile

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()[:6]  # Show first 6 projects
    work_experience = Experience.objects.filter(type='work')
    education = Experience.objects.filter(type='education')
    
    context = {
        'profile': profile,
        'projects': projects,
        'work_experience': work_experience,
        'education': education,
    }
    return render(request, 'portfolio/home.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})