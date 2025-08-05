#from django.contrib import admin
from django.urls import path, include
from . import views
#from equipo.views import ListMiembros, ListTiendas


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('nosotros/', views.nosotros, name="quienes"),
    path('test/', views.test, name='index'),
    path('curiosidades/', views.curiosidades, name="noti_curios"),
    path('eventos/', views.eventos, name="event"),
    path('preguntas/', views.preguntas, name="preguntas"),
    path('contacto/', views.contacto, name="contacto"),
    path('content/', include('news.urls')),
    path('accounts', include('django.contrib.auth.urls')),
    path('accounts', include('registration.urls')),
]

