from django.db import models
from django import forms
from django.forms import DateInput
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field
#from pages.models import Paginas

# products/models.py
from django.db import models

class Product(models.Model):
    PRODUCT_TYPES = [
        ('ecommerce', 'Tienda Virtual'),
        ('inventory', 'Gestión de Inventarios'),
        ('hr', 'Gestión de Capital Humano'),
        ('evaluation', 'Gestión de Evaluaciones'),
        ('service', 'Gestión de Servicios'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, 
                            help_text='Valor único de cada producto creado a partir del nombre', 
                            verbose_name = "Código URL")
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPES)
    description = models.TextField()
    features = models.TextField(help_text="Lista de características separadas por punto y coma")
    benefits = models.TextField(help_text="Lista de beneficios separados por punto y coma")
    business_model = models.TextField()

    def __str__(self):
        return self.name

    def features_list(self):
        return self.features.split(';')
    
    def benefits_list(self):
        return self.benefits.split(';')

class DemoRequest(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField()
    company = models.CharField(max_length=100, verbose_name="Empresa")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    message = models.TextField(blank=True, verbose_name="Descripción de la solicitud")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Demo request for {self.product.name} by {self.name}"