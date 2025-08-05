from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from equipo.models import *

def ListMiembros(request):
    equi = Miembro.objects.all().reverse()
    return render(request, 'About/equipo.html', locals())
