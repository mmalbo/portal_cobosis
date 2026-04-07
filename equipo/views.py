from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from equipo.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
from .models import Profile
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

def profile_pdf(request, username):
    profile = get_object_or_404(Profile, user__username=username, is_public=True)
    context = {
        'profile': profile,
        'educations': profile.educations.all(),
        'experiences': profile.experiences.all(),
        'projects': profile.projects.all().order_by('order'),
        'publications': profile.publications.all(),
        'events': profile.events.all(),
        'awards': profile.awards.all(),
        'skills': profile.skills.all(),
        'certifications': profile.certifications.all(),
        # Si tienes investigaciones:
        # 'investigations': profile.investigations.all(),
    }
    html_string = render_to_string('equipo/perfil_pdf.html', context)
    font_config = FontConfiguration()
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    pdf = html.write_pdf(font_config=font_config)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{profile.user.username}_curriculum.pdf"'
    return response


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