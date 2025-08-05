from django.contrib import admin
from .models import Miembro

# Register your models here.

class MiembroAdmin(admin.ModelAdmin):
    pass

admin.site.register(Miembro, MiembroAdmin)