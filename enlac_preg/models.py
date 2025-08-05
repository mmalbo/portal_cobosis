from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Pregunta(models.Model):
    pregunta = models.CharField(null = False, blank = False, max_length=200, verbose_name="Pregunta")
    respuesta = CKEditor5Field(default = "Texto", verbose_name="Respuesta")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'pregunta'
        verbose_name = "pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ['-created']

    def __str__(self):
        return self.pregunta
    
class Enlaces(models.Model):
    institucion = models.CharField(null = False, blank = False, max_length=200, verbose_name="Entidad de ínteres")
    enlace = models.URLField(null = False, blank = False, verbose_name = "Enlace al que debe visitar")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        db_table = 'enlace'
        verbose_name = "enlace"
        verbose_name_plural = "Enlaces"
        ordering = ['-created']

    def __str__(self):
        return self.institucion
