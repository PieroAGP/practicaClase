from django.urls import path, include
from . import views
from .views import Tareas
urlpatterns = [
    path('', Tareas.as_view(), name='listaTareas'),
    
]