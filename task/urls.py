from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', TaskList.as_view(), name='listaTareas'),
    #changes
    path('task/<int:pk>/', task_detail.as_view(), name='detalle_tarea'),
    path('task/formulario/', NewTask.as_view(), name='formulario'),
    path('task/editarTarea/<int:pk>/', TaskEdit.as_view(),name='editarTarea'),
]