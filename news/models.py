from django.db import models
from django import forms
from django.forms import DateInput
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
#from pages.models import Paginas

class Curio(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = CKEditor5Field(default = "Texto", verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="anuncion_evenet")
    activo = models.BooleanField(verbose_name="Activa",null=True, default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'curiosidades'
        verbose_name = "Curiosidad"
        verbose_name_plural = "Curiosidades"
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/bg-showcase-1.jpg"

class Event(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    description = CKEditor5Field(default = "Texto", verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="Contenido")
    start_time = models.DateTimeField(blank = False, null=True, verbose_name="Fecha del evento")#, widget=forms.DateInput
    end_time = models.DateTimeField(blank = False, null=True, verbose_name="Fecha del evento")
    enlace = models.URLField(null = False, blank = False, verbose_name = "Enlace a las redes", default = "https://produccionesmuhia.ca/eventos/")
    created = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'eventos'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    
    def __str__(self):
        return self.title
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/equipo/generico"

class Comment(models.Model):
    curio = models.ForeignKey('Curio', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text