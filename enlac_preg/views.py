from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pregunta

def show_Preg_Resp(request):
    Preg = Pregunta.objects.all()
    return render(request, 'preg_frec.html', locals())