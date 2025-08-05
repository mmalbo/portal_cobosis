from django.contrib import admin
from .models import imagenes,banner

# Register your models here.

class ImagenesAdmin(admin.ModelAdmin):
    pass

class BannerAdmin(admin.ModelAdmin):
    pass

admin.site.register(imagenes, ImagenesAdmin)
admin.site.register(banner, BannerAdmin)