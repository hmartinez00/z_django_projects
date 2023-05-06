¡Claro! Aquí te muestro los pasos de creación de archivos y directorios, así como el contenido que se debe agregar en cada uno de ellos para la guía 1:

1. Crea un nuevo directorio para el proyecto:

```bash
mkdir myproject
cd myproject
```

2. Crea un entorno virtual y actívalo:

```bash
python3 -m venv env
source env/bin/activate # en Linux/Mac
env\Scripts\activate # en Windows
```

3. Instala Django:

```bash
pip install Django
```

4. Crea un proyecto de Django llamado "mysite":

```bash
django-admin startproject mysite
```

5. En el directorio "mysite", crea una aplicación llamada "polls":

```bash
cd mysite
python manage.py startapp polls
```

6. Agrega el siguiente código al archivo `mysite/settings.py`:

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

7. Agrega el siguiente código al archivo `polls/models.py`:

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

8. Crea las tablas de la base de datos ejecutando las migraciones:

```bash
python manage.py makemigrations polls
python manage.py migrate
```

9. Agrega el siguiente código al archivo `polls/views.py`:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

10. Agrega el siguiente código al archivo `polls/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

11. Agrega el siguiente código al archivo `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

¡Listo! Con estos pasos has creado una aplicación de Django básica.