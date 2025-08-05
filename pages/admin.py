from django.contrib import admin
from .models import Paginas

class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paginas, PageAdmin)