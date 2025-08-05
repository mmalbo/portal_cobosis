from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
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

