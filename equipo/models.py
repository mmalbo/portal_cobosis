from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from registration.models import Profile

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Miembro(models.Model):
    nombre_apellidos = models.CharField(null = False, blank = False, max_length=200, verbose_name="Nombre y apellidos")
    cargo = models.CharField(null = False, blank = False, max_length=200, verbose_name="Cargo")
    descripcion = CKEditor5Field(null = True, default = " ", verbose_name="Reseña")
    foto = models.ImageField(null = True, upload_to="equipo", verbose_name="Foto", default="equipo/generico.png")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'equipo'
        verbose_name = "miembro"
        verbose_name_plural = "Miembros"
        ordering = ['-created']
    
    @property
    def get_image_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return self.foto.url
        else:
            return "/static/img/equipo/generico"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200, verbose_name="Título obtenido")
    institution = models.CharField(max_length=200, verbose_name="Institución")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ubicación")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de finalización")
    is_current = models.BooleanField(default=False, verbose_name="Estudiando actualmente")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Formación académica"
        verbose_name_plural = "Formaciones académicas"
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    position = models.CharField(max_length=200, verbose_name="Cargo")
    company = models.CharField(max_length=200, verbose_name="Empresa/Institución")
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ubicación")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de finalización")
    is_current = models.BooleanField(default=False, verbose_name="Trabajo actual")
    description = CKEditor5Field(
        verbose_name="Descripción del cargo",
        config_name='default'  # Configuración más simple
    )
    achievements = CKEditor5Field(
        blank=True, 
        null=True, 
        verbose_name="Logros principales",
        config_name='default'
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Experiencia profesional"
        verbose_name_plural = "Experiencias profesionales"
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.position} - {self.company}"

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200, verbose_name="Nombre del proyecto")
    role = models.CharField(max_length=100, verbose_name="Rol en el proyecto")
    client = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cliente")
    description = CKEditor5Field(
        verbose_name="Descripción del proyecto",
        config_name='extends'
    )
    technologies = models.CharField(max_length=300, blank=True, null=True, verbose_name="Tecnologías utilizadas")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de finalización")
    duration = models.CharField(max_length=50, blank=True, null=True, verbose_name="Duración")
    link = models.URLField(blank=True, null=True, verbose_name="Enlace al proyecto")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.role}"

class Publication(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=300, verbose_name="Título de la publicación")
    journal = models.CharField(max_length=200, verbose_name="Revista/Medio")
    role = models.CharField(max_length=100, verbose_name="Rol (Autor, Coautor, etc.)")
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)],
        verbose_name="Año de publicación"
    )
    link = models.URLField(blank=True, null=True, verbose_name="Enlace a la publicación")
    description = models.TextField(blank=True, null=True, verbose_name="Resumen")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-year', 'order']
    
    def __str__(self):
        return f"{self.title} ({self.year})"

class Event(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=200, verbose_name="Nombre del evento")
    presentation_title = models.CharField(max_length=300, verbose_name="Título de la ponencia")
    country = models.CharField(max_length=100, verbose_name="País")
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ciudad")
    year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)],
        verbose_name="Año"
    )
    role = models.CharField(max_length=100, default="Ponente", verbose_name="Rol en el evento")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-year', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.presentation_title}"

class Award(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='awards')
    name = models.CharField(max_length=200, verbose_name="Nombre del premio")
    institution = models.CharField(max_length=200, verbose_name="Institución que otorga")
    date = models.DateField(verbose_name="Fecha de otorgamiento")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Premio"
        verbose_name_plural = "Premios"
        ordering = ['-date', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.institution}"

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('TECH', 'Tecnología'),
        ('MANAGEMENT', 'Gestión'),
        ('LANGUAGE', 'Idioma'),
        ('SOFT', 'Habilidades blandas'),
        ('OTHER', 'Otros'),
    ]
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100, verbose_name="Nombre de la habilidad")
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='TECH', verbose_name="Categoría")
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name="Nivel (1-100)",
        help_text="Porcentaje de dominio de la habilidad"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.level}%)"

class Certification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=200, verbose_name="Nombre de la certificación")
    institution = models.CharField(max_length=200, verbose_name="Institución")
    issue_date = models.DateField(verbose_name="Fecha de emisión")
    expiration_date = models.DateField(blank=True, null=True, verbose_name="Fecha de expiración")
    credential_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID de credencial")
    link = models.URLField(blank=True, null=True, verbose_name="Enlace a la certificación")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")
    
    class Meta:
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"
        ordering = ['-issue_date', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.institution}"
    


