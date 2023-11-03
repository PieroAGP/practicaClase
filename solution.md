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
from django.conf import settings 
from django.db import models 
from django.utils import timezone

class task(models.Model): 
    nombre = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    descripcion = models.CharField(max_length=200) 
    realizacion = models.BooleanField(default=False)
    
    
    def _str_(self):
        return self.descripcion
```
### 10. Crear tablas para los modelos en tu base de datos
```bash
python manage.py makemigrations blog
```
