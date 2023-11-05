
from django.db import models 


class Task(models.Model): 
    nombre = models.CharField(max_length=200) 
    descripcion = models.CharField(max_length=200) 
    realizacion = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.nombre)