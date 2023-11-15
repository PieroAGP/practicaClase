
from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
#importamis  la vista
from django.views import View


# Create your views here.

#cambios
class task_detail(View):
   def get(self, request,pk):
      task = get_object_or_404(Task, pk=pk)
      return render(request, 'task/detalle_tarea.html', {'task': task})


class Tareas(View):
  tareas = Task.objects.all()
  template_name="task/listaTareas.html"

  def actualizaTask(self):
    self.tareas = Task.objects.all()
    return self.tareas

  def get(self,request):
    form = TaskForm()
    return render(request,self.template_name,{'tareas': self.actualizaTask(),'form':form})

  def post(self,request):
    form= TaskForm(request.POST)
    if form.is_valid():
         nombre = form.cleaned_data['nombre']
         descripcion= form.cleaned_data['descripcion']
         realizacion= form.cleaned_data['realizacion']
         
         Task.objects.create(nombre=nombre, descripcion=descripcion, realizacion=realizacion)
         return redirect('listaTareas')
    return render(request,self.template_name,{'tareas': self.actualizaTask(),'form':form})

"""

from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
#importamis  la vista
from django.views import View

# Create your views here.

class Tareas(View):
  tareas = Task.objects.all()
  template_name="task/listaTareas.html"

  def actualizaTask(self):
    self.tareas = Task.objects.all()
    return self.tareas

  def get(self,request):
    form = TaskForm()
    return render(request,self.template_name,{'tareas': self.actualizaTask(),'form':form})

  def post(self,request):
    form= TaskForm(request.POST)
    if form.is_valid():
         form.save()
         return redirect('listaTareas')
    return render(request,self.template_name,{'tareas': self.actualizaTask(),'form':form})
"""

#def listaTareas(request):
#    tareas = Task.objects.all()
#    if request.method == 'POST':
##      
##      form = TaskForm(request.POST)
##      if form.is_valid():
##         form.save()
#        return redirect('listaTareas')
#
#     return redirect('listaTareas')  
#
#   else:
#      form= TaskForm()
#   return render(request,'task/listaTareas.html',{'tareas': tareas,'form':form})

