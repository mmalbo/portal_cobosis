from calendar import HTMLCalendar, Calendar
from pkgutil import get_data
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from pages.models import Paginas 
from galeria.models import banner, imagenes, carrusel
from enlac_preg.models import Pregunta, Enlaces
from django.utils.safestring import mark_safe

from .models import *
from equipo.models import *
#from news.utils import Calendar, get_date

#from galeria import imagenes,banner
#from proyectos_muhia.galeria.models import banner
# Create your views here.

def inicio(request):
    """ g_imagenes = imagenes.objects.all()
    sitios = Enlaces.objects.all()
    curios=Curio.objects.all()
    banners = banner.objects.all()
    event = Event.objects.all()
    catalog = carrusel.objects.all() """

    """ Calendario """
    # use today's date for the calendar
    #d = get_date(request.GET.get('day', None))
    # Instantiate our calendar class with today's year and date
    #cal = Calendar(d.year, d.month)
    # Call the formatmonth method, which returns our calendar as a tablewithyear=True
    #html_cal = cal.formatmonth(withyear=True)
    return render(request, "index.html", locals())

def inicio_mant(request):
    return render(request, "pagina_mantenimiento.html", {})

def nosotros(request):
    equi = Miembro.objects.all().reverse()
    return render(request, "about.html", locals())

def test(request):
    return render(request, "index_copy.html", locals())

def curiosidades(request):
    curio=Curio.objects.all()
    return render(request, "noti_curio.html", locals())

def eventos(request):
    events=Event.objects.all()
    return render(request, "event_list.html", locals())

def productos(request):
    g_imagenes = imagenes.objects.all()
    img1 = imagenes.objects.get(pk=1)
    return render(request, "products.html", locals())

def servicios(request):
    return render(request, "service.html", {})

def preguntas(request):
    Preg = Pregunta.objects.all()
    return render(request, "preg_frec.html", locals())

def contacto(request):
    return render(request, "contacto.html", {})
#return HttpResponse("Hola mundo. Al fin tenemos una aplicacion visible.")
