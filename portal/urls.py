#from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from equipo.views import ListMiembros, ListTiendas


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="quienes"),
    path('contacto/', views.contact, name="contacto"),
    path('preguntas/', views.preguntas, name="preguntas"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('catalogo/productos', views.productos, name="catalogo_p"),
    path('catalogo/servicios', views.servicios, name="catalogo_s"),
    
    path('productos/', include('productos.urls')),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts', include('registration.urls')),
    
    path('test/', views.test, name='index'),
    path('test-item/', views.test_item, name='test_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)