Claro, aquí te presento los pasos y comandos a seguir para el tutorial 3 de Django:

1. Abre una terminal y navega hasta el directorio donde quieras crear tu proyecto Django.

```bash
cd /ruta/al/directorio
```

2. Crea un nuevo proyecto de Django.

```bash
django-admin startproject mysite
```

3. Navega hasta el directorio del proyecto y crea una nueva app llamada "polls".

```bash
cd mysite
python manage.py startapp polls
```

4. Abre el archivo `mysite/settings.py` en un editor de texto y agrega `"polls"` en la lista `INSTALLED_APPS`.

```python
INSTALLED_APPS = [
    'polls',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

5. Abre el archivo `polls/models.py` en un editor de texto y define el modelo `Question` y `Choice`.

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

6. Crea las tablas en la base de datos ejecutando la migración.

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Abre el archivo `polls/admin.py` en un editor de texto y agrega el modelo `Question` al sitio de administración.

```python
from django.contrib import admin
from .models import Question

admin.site.register(Question)
```

8. Ejecuta el servidor de desarrollo de Django.

```bash
python manage.py runserver
```

9. Abre tu navegador web e ingresa la dirección `http://127.0.0.1:8000/admin/`. Deberías ver la página de inicio de sesión del sitio de administración de Django.

10. Ingresa las credenciales de superusuario que configuraste al crear el proyecto.

11. Deberías ver la interfaz de administración de Django. Haz clic en el enlace "Questions" para agregar una nueva pregunta.

12. Agrega una pregunta y guarda los cambios.

13. Haz clic en el enlace "Choices" para agregar una nueva opción para la pregunta que acabas de crear.

14. Agrega una opción y guarda los cambios.

15. Ve a la página principal de tu sitio de Django ingresando la dirección `http://127.0.0.1:8000/polls/` en tu navegador web.

16. Deberías ver la lista de preguntas que has agregado.

¡Listo! Ahora tienes un proyecto Django básico con una app "polls" que te permite agregar preguntas y opciones y verlas en la página principal.