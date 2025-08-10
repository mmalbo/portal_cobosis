from calendar import HTMLCalendar, Calendar
from pkgutil import get_data
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils.safestring import mark_safe

from .models import *
from productos.models import *
from equipo.models import *
from pages.models import Paginas 
from galeria.models import banner, imagenes, carrusel
from enlac_preg.models import Pregunta, Enlaces


# Create your views here.

def inicio(request):
    """ g_imagenes = imagenes.objects.all()
    sitios = Enlaces.objects.all()    
    banners = banner.objects.all()
    event = Event.objects.all()
    catalog = carrusel.objects.all() """

    products=Productos.objects.all()
    equip=Miembro.objects.all()

    return render(request, "index.html", locals())

def inicio_mant(request):
    return render(request, "pagina_mantenimiento.html", {})

def nosotros(request):
    equi = Miembro.objects.all().reverse()
    return render(request, "about.html", locals())

def contacto(request):
    return render(request, "contacto.html", {})

def preguntas(request):
    #Preg = Pregunta.objects.all()
    return render(request, "faq.html", locals())

def catalogo(request):
    return render(request, "portfolio-overview.html", {})

def productos(request):
    g_imagenes = imagenes.objects.all()
    img1 = imagenes.objects.get(pk=1)
    return render(request, "products.html", locals())

def servicios(request):
    return render(request, "service.html", {})

def test(request):
    return render(request, "index_copy.html", locals())


#return HttpResponse("Hola mundo. Al fin tenemos una aplicacion visible.")
