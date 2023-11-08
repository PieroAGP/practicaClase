from django.shortcuts import render
from .models import Task
# Create your views here.

def listaTareas(request):
    tareas = Task.objects.all()
    return render(request,'task/listaTareas.html',{'tareas': tareas})

