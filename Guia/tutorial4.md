Por supuesto, aquí está la guía 4 de Django con los pasos detallados, comandos y código:

1. Crea una vista para la página de detalle de la pregunta

Crea un archivo `views.py` dentro de la aplicación `polls`. Agrega el siguiente código:

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

2. Crea una URL para la vista de detalle de la pregunta

Crea un archivo `urls.py` dentro de la aplicación `polls`. Agrega el siguiente código:

```python
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ...
    path('<int:question_id>/', views.detail, name='detail'),
]
```

3. Crea una plantilla para la vista de detalle de la pregunta

Crea una carpeta `templates` dentro de la aplicación `polls`. Crea otra carpeta dentro de `templates` llamada `polls`. Crea un archivo `detail.html` dentro de `polls`. Agrega el siguiente código:

```html
<h1>{{ question.question_text }}</h1>

<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

4. Agrega un enlace a la página de detalle de la pregunta en la página de lista de preguntas

Abre el archivo `polls/templates/polls/index.html`. Agrega un enlace a la página de detalle de la pregunta debajo del enlace "Ver resultados". Agrega el siguiente código:

```html
<li><a href="{% url 'polls:detail' question.id %}">Ver detalles</a></li>
```

5. Ejecuta la aplicación y verifica que todo funcione

Ejecuta el siguiente comando en la terminal para iniciar el servidor web de Django:

```
python manage.py runserver
```

Visita la página de inicio de la aplicación en tu navegador web en la dirección `http://localhost:8000/polls/`. Haz clic en una pregunta para ir a su página de detalle.

¡Listo! Ahora tienes una vista de detalle de la pregunta en tu aplicación de encuestas.