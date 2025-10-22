from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, ContactMessage

def home(request):
    projects = Project.objects.filter(featured=True)[:6]
    skills = Skill.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})
