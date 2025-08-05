import uuid
from django.core.files.base import ContentFile
from base64 import b64decode

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

#Librerías para mensajes, algunos basados en views
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin 

#Librerías para conexión a BD
from django.db import transaction,connection

# Instanciamos las vistas genéricas de Django 
#from django.views import View
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Habilitamos los formularios en Django
from django import forms

from django.utils.decorators import method_decorator

from registration.views import superuser_only
from galeria.models import *
from enlac_preg.models import *
from news.models import *
from pages.models import *
from equipo.models import *

# Create your views here.

#@method_decorator(superuser_only)
def i_admin(request):
    return render(request, "gestion/index.html", {})

def i_herr(request):
    return render(request, "enlace_herramientas.html", {})

#---------- Gestión de banners ----------------
class gestion_banners(ListView):
    model = banner

class crear_banners(SuccessMessageMixin, CreateView):
    model = banner
    form = banner
    fields = "__all__"
    success_message = "Se ha subido correctamente el nuevo promocional."

    def get_success_url(self):
        return reverse('banners')

class detal_banners(DetailView):
    model = banner

class actualizar_banner(SuccessMessageMixin, UpdateView):
    model = banner
    form = banner
    fields = "__all__"
    success_message = "Se ha actualizado correctamente el promocional."

    def get_success_url(self):
        return reverse('banners')

class eliminar_banner(SuccessMessageMixin, DeleteView):
    model = banner
    form = banner
    fields = "__all__"
    print("llegue aqui")

    def get_success_url(self): 
        print("Entro y no hace nada")
        success_message = 'Promocional eliminado correctamente!'
        print("Entro ...")
        messages.success (self.request, (success_message))       
        return reverse('banners') # Redireccionamos a la vista principal

#---------- Gestión de imagenes quienes somos ----------------
class gestion_images(ListView):
    model = imagenes

class crear_images(SuccessMessageMixin, CreateView):
    model = imagenes
    form = imagenes
    fields = "__all__"
    success_message = "Se ha subido correctamente el nuevo promocional."

    def get_success_url(self):
        return reverse('images')

class detal_images(DetailView):
    model = imagenes

class actualizar_images(SuccessMessageMixin, UpdateView):
    model = imagenes
    form = imagenes
    fields = "__all__"
    success_message = "Se ha actualizado correctamente la imagen."

    def get_success_url(self):
        return reverse('images')

class eliminar_images(SuccessMessageMixin, DeleteView):
    model = imagenes
    form = imagenes
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Imagen eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('images') # Redireccionamos a la vista principal
    
#------- Gestión de preguntas ------------------
class gestion_pregunta(ListView):
    model = Pregunta

class crear_pregunta(SuccessMessageMixin, CreateView):
    model = Pregunta
    form = Pregunta
    fields = "__all__"
    success_message = "Se ha subido correctamente la nueva pregunta."

    def get_success_url(self):
        return reverse('pregunta')

class detal_pregunta(DetailView):
    model = Pregunta

class actualizar_pregunta(SuccessMessageMixin, UpdateView):
    model = Pregunta
    form = Pregunta
    fields = "__all__"
    success_message = "Se ha actualizado correctamente la pregunta."

    def get_success_url(self):
        return reverse('pregunta')

class eliminar_pregunta(SuccessMessageMixin, DeleteView):
    model = Pregunta
    form = Pregunta
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Pregunta eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('pregunta') # Redireccionamos a la vista principal

#------- Gestión de Cursiosidades ------------------
class gestion_curiosidades(ListView):
    model = Curio

class crear_curiosidades(SuccessMessageMixin, CreateView):
    model = Curio
    form = Curio
    fields = "__all__"
    success_message = "Se ha subido correctamente la nueva Curiosidad/Noticia."

    def get_success_url(self):
        return reverse('curiosidades')

class detal_curiosidades(DetailView):
    model = Curio

class actualizar_curiosidades(SuccessMessageMixin, UpdateView):
    model = Curio
    form = Curio
    fields = "__all__"
    success_message = "Se ha actualizado correctamente la curiosidad/noticia."

    def get_success_url(self):
        return reverse('curiosidades')

class eliminar_curiosidades(SuccessMessageMixin, DeleteView):
    model = Curio
    form = Curio
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Curiosidad/Noticia eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('curiosidades') # Redireccionamos a la vista principal
    
#------- Gestión de Eventos ------------------
class gestion_eventos(ListView):
    model = Event

class crear_eventos(SuccessMessageMixin, CreateView):
    model = Event
    form = Event
    fields = "__all__"
    success_message = "Se ha subido correctamente el nuevo evento."

    def get_success_url(self):
        return reverse('eventos')

class detal_eventos(DetailView):
    model = Event

class actualizar_eventos(SuccessMessageMixin, UpdateView):
    model = Event
    form = Event
    fields = "__all__"
    success_message = "Se ha actualizado correctamente el evento."

    def get_success_url(self):
        return reverse('eventos')

class eliminar_eventos(SuccessMessageMixin, DeleteView):
    model = Event
    form = Event
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Evento eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('eventos') # Redireccionamos a la vista principal

#------- Gestión de Páginas de Políticas ------------------
class gestion_paginas(ListView):
    model = Paginas

class crear_paginas(SuccessMessageMixin, CreateView):
    model = Paginas
    form = Paginas
    fields = "__all__"
    success_message = "Se ha subido correctamente la nueva página."

    def get_success_url(self):
        return reverse('paginas')

class detal_paginas(DetailView):
    model = Paginas

class actualizar_paginas(SuccessMessageMixin, UpdateView):
    model = Paginas
    form = Paginas
    fields = "__all__"
    success_message = "Se ha actualizado correctamente la página."

    def get_success_url(self):
        return reverse('paginas')

class eliminar_paginas(SuccessMessageMixin, DeleteView):
    model = Paginas
    form = Paginas
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Páginas eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('paginas') # Redireccionamos a la vista principal

#------- Gestión de Enlaces externos ------------------
class gestion_enlaces(ListView):
    model = Enlaces

class crear_enlaces(SuccessMessageMixin, CreateView):
    model = Enlaces
    form = Enlaces
    fields = "__all__"
    success_message = "Se ha subido correctamente el nuevo enlace."

    def get_success_url(self):
        return reverse('enlaces')

class detal_enlaces(DetailView):
    model = Enlaces

class actualizar_enlaces(SuccessMessageMixin, UpdateView):
    model = Enlaces
    form = Enlaces
    fields = "__all__"
    success_message = "Se ha actualizado correctamente el enlace."

    def get_success_url(self):
        return reverse('enlaces')

class eliminar_enlaces(SuccessMessageMixin, DeleteView):
    model = Enlaces
    form = Enlaces
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Enlace eliminado correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('enlaces') # Redireccionamos a la vista principal

#---------- Gestión de equipo ----------------
class gestion_equipo(ListView):
    model = Miembro

class crear_miembro(SuccessMessageMixin, CreateView):
    model = Miembro
    form = Miembro
    fields = "__all__"
    success_message = "Se ha subido correctamente el nuevo promocional."

    def get_success_url(self):
        return reverse('miembros')

class detal_miembro(DetailView):
    model = Miembro

class actualizar_miembro(SuccessMessageMixin, UpdateView):
    model = Miembro
    form = Miembro
    fields = "__all__"
    success_message = "Se ha actualizado correctamente el promocional."

    def get_success_url(self):
        return reverse('miembros')

class eliminar_miembro(SuccessMessageMixin, DeleteView):
    model = Miembro
    form = Miembro
    fields = "__all__"

    def get_success_url(self): 
        print("Entro y no hace nada")
        success_message = 'Promocional eliminado correctamente!'
        print("Entro ...")
        messages.success (self.request, (success_message))       
        return reverse('miembros') # Redireccionamos a la vista principal

#---------- Gestión de imagenes inferiores ----------------
class gestion_images_catalog(ListView):
    model = carrusel

class crear_images_catalog(SuccessMessageMixin, CreateView):
    model = carrusel
    form = carrusel
    fields = "__all__"
    success_message = "Se ha subido correctamente el nuevo promocional."

    def get_success_url(self):
        return reverse('carrusel')

class detal_images_catalog(DetailView):
    model = carrusel

class actualizar_images_catalog(SuccessMessageMixin, UpdateView):
    model = carrusel
    form = carrusel
    fields = "__all__"
    success_message = "Se ha actualizado correctamente la imagen."

    def get_success_url(self):
        return reverse('carrusel')

class eliminar_images_catalog(SuccessMessageMixin, DeleteView):
    model = carrusel
    form = carrusel
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Imagen eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('carrusel') # Redireccionamos a la vista principal

#---------- Gestión de tiendas físicas ----------------
""" class gestion_tiendas(ListView):
    model = Tiendas

class crear_tiendas(SuccessMessageMixin, CreateView):
    model = Tiendas
    form = Tiendas
    fields = "__all__"
    success_message = "Se ha subido correctamente los datos de la nueva tienda."

    def get_success_url(self):
        return reverse('tiendas')

class detal_tiendas(DetailView):
    model = Tiendas

class actualizar_tiendas(SuccessMessageMixin, UpdateView):
    model = Tiendas
    form = Tiendas
    fields = "__all__"
    success_message = "Se ha actualizado correctamente la tienda."

    def get_success_url(self):
        return reverse('tiendas')

class eliminar_tiendas(SuccessMessageMixin, DeleteView):
    model = Tiendas
    form = Tiendas
    fields = "__all__"

    def get_success_url(self): 
        success_message = 'Tienda eliminada correctamente!'
        messages.success (self.request, (success_message))       
        return reverse('tiendas') # Redireccionamos a la vista principal """
