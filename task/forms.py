from django import forms

"""
from .models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields = ['nombre','descripcion','realizacion']
"""
class TaskForm(forms.Form):
    nombre = forms.CharField(label="nombre", max_length = 200)
    descripcion = forms.CharField(label="descripcion",widget=forms.Textarea) 
    realizacion = forms.BooleanField(label="realizacion",required=False)
