from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def listaTareas(request):
    tareas = Task.objects.all()
    if request.method == 'POST':
      form = Task

      return redirect('listaTareas')  

    else:
       form= TaskForm()
    return render(request,'task/listaTareas.html',{'tareas': tareas,'form':form})

