from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Pregunta(models.Model):
    text = models.CharField(null = False, blank = False, default='', max_length=200, verbose_name="Pregunta")
    #respuesta = CKEditor5Field(default = "Texto", verbose_name="Respuesta")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'pregunta'
        verbose_name = "pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ['-created']

    def __str__(self):
        return self.text
    
class Respuesta(models.Model):
    #pregunta = models.CharField(null = False, blank = False, default='', max_length=200, verbose_name="Pregunta")
    text = CKEditor5Field(default = "Texto", verbose_name="Respuesta")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'respuesta'
        verbose_name = "respuesta"
        verbose_name_plural = "Respuestas"
        ordering = ['-created']

    def __str__(self):
        return self.text
    
class FAQ(models.Model):
    pregunta = models.ForeignKey(Pregunta, null=False, on_delete=models.CASCADE, verbose_name="Pregunta") 
    respuesta = models.ForeignKey(Respuesta, null=True, on_delete=models.CASCADE, verbose_name='Respuesta')
    etiqueta = models.CharField(max_length=200, verbose_name='etiquetas para la búsqeda y relaciones')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        db_table = 'faq'
        verbose_name = "faq"
        verbose_name_plural = "FAQs"
        ordering = ['-created']

    def __str__(self):
        return self.text
    
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
