from django.urls import path
from django.contrib import admin

from gestion.views import *
""" gestion_banners,eliminar_banner,crear_banners,actualizar_banner
from gestion.views import gestion_images, eliminar_images,crear_images,actualizar_images
from gestion.views import gestion_pregunta, eliminar_pregunta,crear_pregunta,actualizar_pregunta
from gestion.views import gestion_curiosidades, eliminar_curiosidades,crear_curiosidades,actualizar_curiosidades
from gestion.views import gestion_eventos, eliminar_eventos, crear_eventos,actualizar_eventos
from gestion.views import gestion_paginas, eliminar_paginas, crear_paginas,actualizar_paginas
from gestion.views import gestion_enlaces, eliminar_enlaces, crear_enlaces,actualizar_enlaces
from gestion.views import gestion_equipo, eliminar_miembro, crear_miembro,actualizar_miembro
from gestion.views import gestion_images_catalog, eliminar_images_catalog,crear_images_catalog,actualizar_images_catalog """

from . import views


urlpatterns = [
    path('', views.i_admin, name='gestion'),
    path('herramientas/', views.i_herr, name='herramientas'),
#---------- Gestión de banners ----------------
    path('banners/', gestion_banners.as_view( template_name="gestion/banners.html"), name='banners'),
    path('banners/eliminar/<int:pk>', eliminar_banner.as_view(), name='eliminar_banner'),
    path('banners/crear', crear_banners.as_view(template_name = "gestion/banners_crear.html"), name='crear_banner'),
    path('banners/editar/<int:pk>', actualizar_banner.as_view(template_name = "gestion/banners_actualizar.html"), name='actualizar_banner'),
    #---------- Gestión de imagenes ----------------
    path('images/', gestion_images.as_view( template_name="gestion/images.html"), name='images'),
    path('images/eliminar/<int:pk>', eliminar_images.as_view(), name='eliminar_images'),
    path('images/crear', crear_images.as_view(template_name = "gestion/images_crear.html"), name='crear_images'),
    path('images/editar/<int:pk>', actualizar_images.as_view(template_name = "gestion/images_actualizar.html"), name='actualizar_images'),
    #------- Gestión de preguntas ------------------
    path('pregunta/', gestion_pregunta.as_view( template_name="gestion/pregunta.html"), name='pregunta'),
    path('pregunta/eliminar/<int:pk>', eliminar_pregunta.as_view(), name='eliminar_pregunta'),
    path('pregunta/crear', crear_pregunta.as_view(template_name = "gestion/pregunta_crear.html"), name='crear_pregunta'),
    path('pregunta/editar/<int:pk>', actualizar_pregunta.as_view(template_name = "gestion/pregunta_actualizar.html"), name='actualizar_pregunta'),
    #------- Gestión de curiosidades ------------------
    path('curiosidades/', gestion_curiosidades.as_view( template_name="gestion/curiosidades.html"), name='curiosidades'),
    path('curiosidades/eliminar/<int:pk>', eliminar_curiosidades.as_view(), name='eliminar_curiosidades'),
    path('curiosidades/crear', crear_curiosidades.as_view(template_name = "gestion/curiosidades_crear.html"), name='crear_curiosidades'),
    path('curiosidades/editar/<int:pk>', actualizar_curiosidades.as_view(template_name = "gestion/curiosidades_actualizar.html"), name='actualizar_curiosidades'),
    #------- Gestión de eventos ------------------
    path('eventos/', gestion_eventos.as_view( template_name="gestion/eventos.html"), name='eventos'),
    path('eventos/eliminar/<int:pk>', eliminar_eventos.as_view(), name='eliminar_eventos'),
    path('eventos/crear', crear_eventos.as_view(template_name = "gestion/eventos_crear.html"), name='crear_eventos'),
    path('eventos/editar/<int:pk>', actualizar_eventos.as_view(template_name = "gestion/eventos_actualizar.html"), name='actualizar_eventos'),
    #------- Gestión de paginas de políticas ------------------
    path('paginas/', gestion_paginas.as_view( template_name="gestion/paginas.html"), name='paginas'),
    path('paginas/eliminar/<int:pk>', eliminar_paginas.as_view(), name='eliminar_paginas'),
    path('paginas/crear', crear_paginas.as_view(template_name = "gestion/paginas_crear.html"), name='crear_paginas'),
    path('paginas/editar/<int:pk>', actualizar_paginas.as_view(template_name = "gestion/paginas_actualizar.html"), name='actualizar_paginas'),
    #------- Gestión de enlaces externos ------------------
    path('enlaces/', gestion_enlaces.as_view( template_name="gestion/enlaces.html"), name='enlaces'),
    path('enlaces/eliminar/<int:pk>', eliminar_enlaces.as_view(), name='eliminar_enlaces'),
    path('enlaces/crear', crear_enlaces.as_view(template_name = "gestion/enlaces_crear.html"), name='crear_enlaces'),
    path('enlaces/editar/<int:pk>', actualizar_enlaces.as_view(template_name = "gestion/enlaces_actualizar.html"), name='actualizar_enlaces'),
    #---------- Gestión de equipo ----------------
    path('miembros/', gestion_equipo.as_view( template_name="gestion/equipo.html"), name='miembros'),
    path('miembros/eliminar/<int:pk>', eliminar_miembro.as_view(), name='eliminar_miembro'),
    path('miembros/crear', crear_miembro.as_view(template_name = "gestion/miembro_crear.html"), name='crear_miembro'),
    path('miembros/editar/<int:pk>', actualizar_miembro.as_view(template_name = "gestion/miembro_actualizar.html"), name='actualizar_miembro'),
    #---------- Gestión de imagenes galeria inferior----------------
    path('images_catalog/', gestion_images_catalog.as_view( template_name="gestion/catalog.html"), name='carrusel'),
    path('images_catalog/eliminar/<int:pk>', eliminar_images_catalog.as_view(), name='eliminar_carrusel'),
    path('images_catalog/crear', crear_images_catalog.as_view(template_name = "gestion/catalog_crear.html"), name='crear_carrusel'),
    path('images_catalog/editar/<int:pk>', actualizar_images_catalog.as_view(template_name = "gestion/catalog_actualizar.html"), name='actualizar_carrusel'),
    

]