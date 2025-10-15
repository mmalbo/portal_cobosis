from django.db import models
from django.db import models
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_ckeditor_5.fields import CKEditor5Field

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = "Usuario")
    avatar = models.ImageField(upload_to='profiles', null=True, blank=True, verbose_name = "Foto")
    cargo = CKEditor5Field(verbose_name="Cargo actual", config_name='default', blank=True, null=True)
    bio = CKEditor5Field(default = "Texto", null=True, blank=True, verbose_name="Biografía")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name = "Enlace")
    title = models.CharField(max_length=200, verbose_name="Título profesional", null=True, blank=True,)
    location = models.CharField(max_length=100, verbose_name="Ubicación", null=True)
    email = models.EmailField(verbose_name="Email de contacto", null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    
    # Redes sociales
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    twitter = models.URLField(blank=True, null=True, verbose_name="Twitter")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub")
    website = models.URLField(blank=True, null=True, verbose_name="Sitio web personal")
    
    # Campos de control
    is_public = models.BooleanField(default=True, verbose_name="Perfil público")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = ['user__first_name', 'user__last_name']
    
    @property
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.title}"
    
    @property
    def get_image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/images/equipo_generico"

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
