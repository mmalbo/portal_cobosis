from os import path
from django.conf import settings
from django.contrib import admin
from . import views
#from main import views

urlpatterns = [
    path('', views.show_Preg_Resp , name='preg_resp'),
]