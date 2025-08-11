#from calendar import HTMLCalendar, Calendar
from pkgutil import get_data
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from django.http import HttpResponse
from datetime import datetime
from django.utils.safestring import mark_safe

from .models import *
from .forms import *
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

def contact(request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = contact_form(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            tlf = request.POST.get('tlf', '')
            content = request.POST.get('content', '')
            
            e_mail = EmailMessage(
                "CoBoSis: Nuevo mensaje de la página",
                "De {} <{}>\n\n{}".format(name, email, tlf, content),
                ['ycocab@gmail.com'],
            )
            try:
                e_mail.send()
                print("ok")
                return redirect(reverse('contacto'), "?ok")
            except:
                return redirect(reverse('contacto'), "?fail")
    return render(request, "contacto.html", {'form':contact_form})

def preguntas(request):
    #Preg = Pregunta.objects.all()
    return render(request, "faq.html", locals())

def catalogo(request):
    products=Productos.objects.all()
    return render(request, "portfolio-overview.html", locals())

def productos(request):
    products=Productos.objects.all()
    return render(request, "portfolio-productos.html", locals())

def servicios(request):
    products=Productos.objects.all()
    return render(request, "portfolio-servicios.html", locals())

def test(request):
    return render(request, "index_copy.html", locals())

def test_item(request):
    return render(request, "portfolio-item.html", locals())


#return HttpResponse("Hola mundo. Al fin tenemos una aplicacion visible.")
