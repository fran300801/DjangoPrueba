from django.urls import path
from . import views

urlpatterns = [

    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('listarTareas/', views.listarTareas, name='listarTareas'),
    path('listarTareasID/<int:id>/', views.listarTareasID, name='listarTareasID'),
    path('listarTareaMejorado/<int:id>/', views.listarTareaMejorado, name='listarTareasMejorado'),
    path('listarTareaCompletada/', views.listarTareaCompletada, name='listarTareaCompletada'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('crear_programador/', views.crear_programador, name='crear_programador'),

]