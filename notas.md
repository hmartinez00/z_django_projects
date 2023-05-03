1. django-admin startproject proyecto

2. cd .\proyecto

    probar cambio: python .\manage.py runserver
    Detener servidor.

3. Crear la base de datos para crear la tabla "auth_user".

    3.1 python .\manage.py migrate

    3.2 python .\manage.py createsuperuser

    3.3 Introducir los datos solicitados:

    3.4 probar cambio: python .\manage.py runserver

    Acceder a: http://127.0.0.1:8000/admin/
    Detener servidor.

4. Creacion de una App:

    4.1 python .\manage.py startapp aplicacion

    4.2 Actualizacion settings.py

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'aplicacion',
    ]
    ```

    4.3 Actualizacion:

        proyecto/urls.py

        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('aplicacion/', include('aplicacion.urls')),
        ]
        ```

        Creacion: proyecto/aplicacion/urls.py

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
       
    4.4 Actualizacion:
        proyecto/aplicacion/views.py

    ```python
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')
    ```


5. Creacion: proyecto/template
Actualizacion proyecto/settings.py

    TEMPLATES: DIRS

    ```python
    #...
    import os
    #...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'aplicacion', 'templates')],
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

    DATABASES

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

    LANGUAGE_CODE

    ```python
    LANGUAGE_CODE = 'es-eu'
    ```

    probar cambio: python .\manage.py runserver
    Detener servidor.


4.5 Actualizacion:
    proyecto/aplicacion/models.py
    proyecto/aplicacion/admin.py


python .\manage.py makemigrations aplicacion




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