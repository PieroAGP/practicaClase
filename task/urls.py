from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', Tareas.as_view(), name='listaTareas'),
    #changes
    path('task/<int:pk>/', task_detail.as_view(), name='detalle_tarea'),
    path('formulario/', Tareas.as_view(), name='formulario')
]