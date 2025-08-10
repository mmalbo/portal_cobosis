from django.contrib import admin
from .models import DemoRequest, Productos

class ProductAdmin(admin.ModelAdmin):
    pass

""" class DemoRequestAdmin(admin.ModelAdmin):
    pass """

#admin.site.register(DemoRequest, DemoRequest)
admin.site.register(Productos, ProductAdmin)