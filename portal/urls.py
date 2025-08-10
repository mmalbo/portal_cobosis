#from django.contrib import admin
from django.urls import path, include
from . import views
#from equipo.views import ListMiembros, ListTiendas


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="quienes"),
    path('contacto/', views.contacto, name="contacto"),
    path('preguntas/', views.preguntas, name="preguntas"),
    path('catalogo/', views.catalogo, name="catalogo"),
    
    path('productos/', include('productos.urls')),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts', include('registration.urls')),
    
    path('test/', views.test, name='index'),
]

