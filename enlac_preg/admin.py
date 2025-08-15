from django.contrib import admin
from .models import Enlaces,Pregunta, FAQ, Respuesta

# Register your models here.

class EnlacesAdmin(admin.ModelAdmin):
    pass

class PreguntasAdmin(admin.ModelAdmin):
    pass

class RespuestaAdmin(admin.ModelAdmin):
    pass

class FAQAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enlaces, EnlacesAdmin)
admin.site.register(Pregunta, PreguntasAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(FAQ, FAQAdmin)
