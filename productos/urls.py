# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('productos/list/', views.catalogo_prod, name='catalogo_prod'),
    path('productos/<slug:slug>/', views.product_detail, name='detalle_prod'),
    # Agregar rutas similares para otros productos...
]