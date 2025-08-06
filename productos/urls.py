# products/urls.py
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('tienda-virtual/', views.product_detail, 
         {'slug': 'tienda-virtual'}, name='ecommerce_detail'),
    path('inventory/', views.product_detail, 
         {'slug': 'gippro'}, name='inventory_detail'),
    # Agregar rutas similares para otros productos...
]