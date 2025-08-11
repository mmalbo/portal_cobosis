from django.contrib import admin
from .models import Enlaces, Pregunta, Respuesta, FAQ

# Register your models here.

class EnlacesAdmin(admin.ModelAdmin):
    pass

class PreguntaAdmin(admin.ModelAdmin):
    pass

class RespuestasAdmin(admin.ModelAdmin):
    pass

class FAQAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enlaces, EnlacesAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestasAdmin)
admin.site.register(FAQ, FAQAdmin)
