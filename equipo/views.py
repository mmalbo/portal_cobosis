from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from equipo.models import *
from django.contrib.auth.decorators import login_required


def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username, is_public=True)
    
    context = {
        'profile': profile,
        'educations': profile.educations.all(),
        'experiences': profile.experiences.all(),
        'projects': profile.projects.all(),
        'publications': profile.publications.all(),
        'events': profile.events.all(),
        'awards': profile.awards.all(),
        'skills': profile.skills.all(),
        'certifications': profile.certifications.all(),
    }
    
    return render(request, 'equipo/perfil.html', context)

@login_required
def my_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return profile_detail(request, request.user.username)

def ListMiembros(request):
    equi = Profile.objects.all().reverse()
    return render(request, 'About/equipo.html', locals())

def perfilBase(request):
    return render(request, 'equipo/perfil.html', locals())