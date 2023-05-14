import os
from django.apps import apps
from django.db import models
from django.utils import timezone


def create_model(app_name, model_name, fields):
    # Obtenemos la aplicación a la que queremos agregar el modelo
    app_config = apps.get_app_config(app_name)

    # Definimos los campos del modelo
    attrs = {
        '__module__': app_config.__module__,
        'created_at': models.DateTimeField(default=timezone.now)
    }
    attrs.update(fields)

    # Creamos la clase del modelo y la registramos en la aplicación
    model_class = type(model_name, (models.Model,), attrs)
    app_config.models_module.models[model_name] = model_class

    # Guardamos el archivo del modelo en la carpeta correspondiente
    models_path = os.path.join(app_config.path, 'models.py')
    with open(models_path, 'a') as f:
        f.write(f'\n\n{model_class.__name__} = {model_class.__name__}')
    
    # Creamos la migración y la aplicamos
    os.system(f'python manage.py makemigrations {app_name}')
    os.system('python manage.py migrate')
