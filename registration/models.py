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
    bio = CKEditor5Field(default = "Texto", null=True, blank=True, verbose_name="Biografía")
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name = "Enlace")

    @property
    def name(self):
        return self.user.first_name
    
    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/user.png"

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su pefil enlazado.")
