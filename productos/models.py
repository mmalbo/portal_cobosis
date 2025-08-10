from django.db import models
from django import forms
from django.forms import DateInput
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
#from pages.models import Paginas

# products/models.py

def custom_upload_to(instance, filename):
    old_instance = Productos.objects.get(pk=instance.pk)
    old_instance.images.delete()
    return 'productos_images/' + filename

class Productos(models.Model):
    """ PRODUCT_TYPES = [
        ('comercio-e', 'Tienda Virtual'),
        ('inventario', 'Gestión de Inventarios'),
        ('rrhh', 'Gestión de Capital Humano'),
        ('evaluacion', 'Gestión de Evaluaciones'),
        ('servicio', 'Gestión de Servicios'),
    ] """
    
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, 
                            help_text='Valor único de cada producto creado a partir del nombre', 
                            verbose_name = "Código URL")
    #product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    slogan = models.TextField(max_length=250)
    descripcion = models.TextField(max_length=350)
    caracteristicas = models.TextField(help_text="Lista de características separadas por punto y coma")
    beneficios = models.TextField(help_text="Lista de beneficios separados por punto y coma")
    modelo_negocio = models.TextField()
    images = models.ImageField(upload_to='productos_images', null=True, blank=True, verbose_name = "Logo o imagen")
    servicio = models.BooleanField(default=False, verbose_name = "Servicio")
    destacado = models.BooleanField(default=True, verbose_name = "Destacar en Front")

    def __str__(self):
        return self.nombre

    def features_list(self):
        return self.caracteristicas.split(';')
    
    def benefits_list(self):
        return self.beneficios.split(';')

    @property
    def get_image_url(self):
        if self.images and hasattr(self.images, 'url'):
            return self.images.url
        else:
            return "/static/images/Generico.png"

class DemoRequest(models.Model):
    product = models.ForeignKey(Productos, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField()
    company = models.CharField(max_length=100, verbose_name="Empresa")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    message = models.TextField(blank=True, verbose_name="Descripción de la solicitud")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Demo request for {self.product.name} by {self.name}"