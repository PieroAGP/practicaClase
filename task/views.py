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

