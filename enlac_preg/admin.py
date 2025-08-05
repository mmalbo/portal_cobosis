from django.contrib import admin
from .models import Enlaces,Pregunta

# Register your models here.

class EnlacesAdmin(admin.ModelAdmin):
    pass

class PreguntasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enlaces, EnlacesAdmin)
admin.site.register(Pregunta, PreguntasAdmin)
