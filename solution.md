# Pasos
### 1. Creamos un entorno virtual
```bash
mkvirtualenv nombreEntorno
```
### 2. Creacion del requirements
creamos un archivo txt con lo siguiente´
```txt
Django~=4.2.7
```
### 3. Instalamos el requirements con ayuda de pip
```bash
pip install -r requirements.txt
```
### 4. Creamos un .gitignore para no tener problemas con GitHub más adelante con el siguiente contenido
```txt
*.pyc
*~
__pycache__
db.sqlite3
/static
.DS_Store
```
### 5. Creamos el esqueleto del proyecto
```bash
django-admin startproject mysite . 
```
### 6. Cambiamos en settings
```python
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

STATIC_ROOT = BASE_DIR / 'static'
```

### 7. Crear la aplicacion task
```bash
python manage.py startapp task
```
### 8. En mysite/settings.py, en la parte de Installed_apps añadimos lo siguiente 
```python
'task.apps.TaskConfig'
```
### 9. Crear el modelo de task
```python

from django.db import models 


class Task(models.Model): 
    nombre = models.CharField(max_length=200) 
    descripcion = models.CharField(max_length=200) 
    realizacion = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.nombre)
```
### 10. Preparar las tablas para añadirlas a la BBDD, y hacer el cambio definitivo.
```bash
python manage.py makemigrations task
```
```bash
python manage.py migrate task
```
### 11. Preparar las URLS
En mysite, añadimos al archivo urls.py lo siguiente:
```python
from django.urls import path, include

path('',include('task.urls')),
```
Creamos el archivo urls.py en task y añadimos lo siguinete
```python
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.listaTareas, name='listaTareas'),

]
```

### 12. Modificar views.py
en el archivo añadir lo siguiente:
```python
from django.shortcuts import render
from .models import Task
# Create your views here.

def listaTareas(request):
    tareas = Task.objects.all()
    return render(request,'listaTareas.html',{'tareas': tareas})
```

### 13. Templates
Creamos una carpeta llamada templates, dentro de creamos un archivo con el nombre de listaTareas.html y deberia de quear con el siguiente contenido
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista Tareas</title>
</head>
<body>
    <h1>Tareas de Piero</h1>
    <ol>
        {% for tarea in tareas %}
            <li> 
                Nombre: {{tarea.nombre}} <br>
                Descripcion: {{tarea.descripcion}} <br>
                Realizacion: {{tarea.realizacion|yesno:"SI,NO"}} <br>
            </li>
            {% empty %}
            <li>
                No hay tareas por hacer
            </li>
        {%endfor%}    
    </ol>
</body>
</html>
```
### 14 Administrador de Django
Completamos el archivo admin.py y deberia de quear asi:
```python
from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
```

Creamos un super usuario
```bash
python manage.py createsuperuser
``` 
completamos los campos con nombreUsuario, correo, password