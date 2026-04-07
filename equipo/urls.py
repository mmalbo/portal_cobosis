from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin
from equipo import views

urlpatterns = [
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('perfil/', views.perfilBase, name='perfil'),
    path('perfil/<str:username>/pdf/', views.profile_pdf, name='profile_pdf'),
]