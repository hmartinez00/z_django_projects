# Ciclo de creacion de un proyecto con Django 4

## 1. Creando el proyecto

* 1.1 
django-admin startproject mysite
* 1.2 
cd .\mysite
> probar cambio: 
* 1.3 
python .\manage.py runserver
> Detener servidor.

## 2. Crear la base de datos para crear la tabla "auth_user".

* 2.1 
python .\manage.py migrate
* 2.2 
python .\manage.py createsuperuser
* 2.3 Introducir los datos solicitados: probar cambio
* 2.4 
python .\manage.py runserver

* 2.5 Acceder a: 
http://127.0.0.1:8000/admin/
> Detener servidor.

4. ## Creacion de una App:

* 4.1
python .\manage.py startapp polls

* 4.2 Actualizacion settings.py

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'polls',
    ]
    ```

* 4.3 Actualizacion:

    proyecto/urls.py

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('polls/', include('polls.urls')),
    ]
    ```

    Creacion: proyecto/polls/urls.py

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
       
* 4.4 Actualizacion:
proyecto/polls/views.py

    ```python
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')
    ```


## 5. Crear directorio template
Creacion: proyecto/template

## 6. Actualizacion de ajustes, modelos, panel administrativo
Actualizacion proyecto/settings.py

* 6.1 TEMPLATES: DIRS

    ```python
    #...
    import os
    #...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'polls', 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

* 6.2 DATABASES

    ```python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'vrss_operation_and_managment_subsystem',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

* 6.3 LANGUAGE_CODE

    ```python
    LANGUAGE_CODE = 'es-eu'
    ```

* 6.4 probar cambio: 
python .\manage.py runserver

> Detener servidor.

* 6.5 Actualizacion:
    proyecto/polls/models.py
    proyecto/polls/admin.py


python .\manage.py makemigrations polls




PARA CREAR NUEVAS VISTAS:

Por supuesto, aquí te muestro los pasos a seguir para agregar una nueva vista que renderice un archivo HTML en Django:

1. Abrir el archivo `views.py` de la aplicación donde se quiere agregar la nueva vista.
2. Importar las librerías necesarias para renderizar una plantilla de HTML. Por ejemplo, podrías importar `render` de la siguiente forma:
   ```python
   from django.shortcuts import render
   ```
3. Agregar una nueva función en `views.py` para definir la lógica de la vista. Por ejemplo, podrías agregar la siguiente función:
   ```python
   def new_view(request):
       return render(request, 'new.html')
   ```
   En este caso, `new_view` es el nombre de la nueva vista y `new.html` es el nombre del archivo HTML que se quiere renderizar.
4. Abrir el archivo `urls.py` de la aplicación y agregar una nueva ruta para la nueva vista. Por ejemplo, podrías agregar la siguiente línea de código:
   ```python
   path('new/', views.new_view, name='new')
   ```
   En este caso, `new/` es el nombre de la ruta para la nueva vista y `views.new_view` hace referencia a la función `new_view` que se creó en `views.py`. También se le da un nombre a la ruta usando el parámetro `name`.
5. Crear un archivo HTML en el directorio `templates` de la aplicación. Por ejemplo, podrías crear un archivo llamado `new.html` con el siguiente contenido:
   ```html
   <h1>Nueva vista</h1>
   <p>Este es un ejemplo de una nueva vista.</p>
   ```
6. Ejecutar el comando `makemigrations` para crear una nueva migración que incluya los cambios realizados en `views.py` y `urls.py`.
7. Ejecutar el comando `migrate` para aplicar los cambios a la base de datos.
8. Iniciar el servidor para ver la nueva vista en el navegador.

Espero que estos pasos te sean útiles. Si tienes alguna otra pregunta, no dudes en preguntarme.


AGREGAR NUEVA APLICACION:

Si deseas agregar una nueva aplicación a un proyecto Django, estos son los pasos que debes seguir:

1. Ejecuta el comando `python manage.py startapp nombre_de_la_aplicacion` para crear el directorio de la nueva aplicación con su estructura inicial.

2. Agrega la nueva aplicación a la lista `INSTALLED_APPS` del archivo `settings.py` del proyecto.

3. Define las rutas (URLs) de la nueva aplicación en su archivo `urls.py` en la aplicación.

4. Define las vistas de la nueva aplicación en su archivo `views.py`.

5. Define las plantillas HTML en el directorio `templates` de la nueva aplicación.

6. Actualiza las migraciones y aplica los cambios a la base de datos mediante los comandos `python manage.py makemigrations` y `python manage.py migrate`.

7. Agrega lógica a las vistas y plantillas HTML de la nueva aplicación según sea necesario.

8. Testea la nueva aplicación y asegúrate de que todo funcione correctamente.