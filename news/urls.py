from django.urls import path
from .views import CuriosViews, CalendarView, Comment_Add

urlpatterns = [
    path('<int:pk>', CuriosViews.as_view(template_name = "curiosidades.html")),
    #Agregar URL de Agregar nuevo comentario
    path('crear_comentario$<int:pk>', Comment_Add.as_view(template_name = "gestion/comentario_crear.html"), name = "agregar_comentario"), 
    #path('calendario/', CalendarView.as_view(), name='calendar'),, name="curios"
]