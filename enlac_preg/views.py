from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pregunta, Respuesta, FAQ

""" def show_Preg_Resp(request):
    Preg = FAQ.objects.all()
    
    print(Preg.first)
    return render(request, 'faq.html', locals()) """