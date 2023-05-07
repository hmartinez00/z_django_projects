# Escribiendo tu primera aplicación Django, parte 1

## Crear el proyecto

django-admin startproject mysite
cd .\mysite

### Activar el servidor
python .\manage.py runserver

### Crear la app
py manage.py startapp polls

### Escribir la primera vista

* Abrir `polls/views.py` y colocar este codigo:

    ```python
    from django.http import HttpResponse


    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    ```

* Crear el archivo `polls/urls.py` y colocar el siguiente codigo:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.index, name="index"),
    ]
    ```

* Modificar el archivo `mysite/urls.py` y colocar el siguiente codigo:

    ```python
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("polls/", include("polls.urls")),
    ]
    ```

Con este paso haz incorporado todas las vistas de la aplicacion "polls".

* Probar los cambios:
py manage.py runserver

* Entrar a la vista mediante la siguiente direccion en el navegador:
http://127.0.0.1:8000/polls/



# Escribiendo tu primera aplicación Django, parte 2

## Database setup

### Creando los modelos
python manage.py migrate

* Abre `polls/models.py` y colocar el siguiente codigo:

    ```python
    from django.db import models


    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField("date published")


    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
    ```

### Instalando la aplicacion

* Abre `mysite/settings.py` y colocar el siguiente codigo:

    ```python
    INSTALLED_APPS = [
        "polls.apps.PollsConfig",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    ```

La clase `PollsConfig` está en el archivo `polls/apps.py`

### Haciendo las migraciones
python manage.py makemigrations polls
python manage.py migrate

## Jugando con la API

### Primeras modificaciones
* python manage.py shell

```md
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>

# Exit
>>> quit()
```

* Modificaremos `polls/models.py` agregando las def a las clases existentes:

```python
from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

```

* Agregar ademas el siguiente metodo:

```python
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
```

### Segundas modificaciones
* python manage.py shell

```md
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
>>> quit()
```

## Crear un usuario administrador 
python manage.py createsuperuser

* Introduzca los datos solicitados.

### Iniciar el servidor de desarrollo
python manage.py runserver

* Abrir la siguiente direccion del panel administrativo:
http://127.0.0.1:8000/admin/

## Hacer que la aplicación de encuestas sea modificable en el administrador

* Abra `polls/admin.py` y colocar el siguiente codigo.

    ```python
    from django.contrib import admin

    from .models import Question

    admin.site.register(Question)
    ```

# Escribiendo tu primera aplicación Django, parte 3

## Escribiendo más vistas

* Abra `polls/views.py` y colocar el siguiente codigo:

    ```python
    #...
    def detail(request, question_id):
        return HttpResponse("You're looking at question %s." % question_id)


    def results(request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)


    def vote(request, question_id):
        return HttpResponse("You're voting on question %s." % question_id)
    ```

* Modificar el archivo `polls/urls.py` y colocar el siguiente codigo:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        # ex: /polls/
        path("", views.index, name="index"),
        # ex: /polls/5/
        path("<int:question_id>/", views.detail, name="detail"),
        # ex: /polls/5/results/
        path("<int:question_id>/results/", views.results, name="results"),
        # ex: /polls/5/vote/
        path("<int:question_id>/vote/", views.vote, name="vote"),
    ]
    ```

## Escribir vistas que realmente hagan algo

* Abra `polls/views.py` y modificar el contenido como sigue: 

    ```python
    from django.http import HttpResponse

    from .models import Question


    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        output = ", ".join([q.question_text for q in latest_question_list])
        return HttpResponse(output)


    # Leave the rest of the views (detail, results, vote) unchanged
    ```

* Crear `polls/templates/polls/index.html`

* Ponga el siguiente código en esa plantilla:

    ```python
    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}
    ```

* Ahora actualicemos nuestra vista `polls/views.py` para usar la plantilla:

    ```python
    from django.http import HttpResponse
    from django.template import loader

    from .models import Question


    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        template = loader.get_template("polls/index.html")
        context = {
            "latest_question_list": latest_question_list,
        }
        return HttpResponse(template.render(context, request))
    ```

## Un atajo: render()

* Ahora actualicemos nuestra vista `polls/views.py`:

    ```python
    from django.shortcuts import render

    from .models import Question


    def index(request):
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        context = {"latest_question_list": latest_question_list}
        return render(request, "polls/index.html", context)
    ```


## Generando un error 404

* Ahora actualicemos nuestra vista `polls/views.py`:

    ```python
    from django.http import Http404
    from django.shortcuts import render

    from .models import Question


    # ...
    def detail(request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, "polls/detail.html", {"question": question})
    ```

## Un atajo: get_object_or_404()

* Ahora actualicemos nuestra vista `polls/views.py`:

    ```python
    from django.shortcuts import get_object_or_404, render

    from .models import Question


    # ...
    def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, "polls/detail.html", {"question": question})
    ```

## Utilice el sistema de plantillas

Vuelva a la vista `detail()` para nuestra aplicación encuesta. Teniendo en cuenta la variable de contexto question, así es como la plantilla `polls/detail.html` podría verse:

```python
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```



## Quitar URLs codificadas de manera predeterminada en las plantillas

Recuerde que cuando escribimos el enlace para una pregunta en la plantilla polls/index.html, el enlace estaba parcialmente codificado de forma predeterminada como este:

<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>

El problema con este método de codificación predeterminada y estrechamente acoplada es que se hace difícil modificar las URLs en proyectos que tengan muchas plantillas. Sin embargo, puesto que usted definió el argumento de nombre en las funciones path() en el módulo polls.urls, usted puede eliminar la dependencia en rutas URL específicas definida en su configuración de URL usando la etiqueta de plantilla {% url %}:

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

La forma como esto funciona es buscando la definición de la URL como se específica en el módulo polls.urls. Usted puede ver exactamente donde se define el nombre de la URL de “detail” a continuación:

```md
# the 'name' value as called by the {% url %} template tag
path("<int:question_id>/", views.detail, name="detail"),
```

Si desea modificar la URL de la vista de detalle de las encuestas a algo diferente, quizás a algo como polls/specifics/12/, en lugar de hacerlo en la plantilla (o plantillas), usted la modificaría en polls/urls.py:

```md
# added the word 'specifics'
path("specifics/<int:question_id>/", views.detail, name="detail"),
```

## Asignando los nombres de URLs

El proyecto tutorial solo tiene una aplicación; polls. En proyectos reales de Django, puede haber cinco, diez, veinte o más aplicaciones. ¿Cómo diferencia Django los nombres de las URLs entre ellos? Por ejemplo, la aplicación polls tiene una vista detail, como la podría tener también una aplicación en el mismo proyecto que es para un blog. ¿Cómo hacer para que Django sepa cual vista de aplicaciones crear para una URL cuando se utiliza la etiqueta de plantilla`` {% url%}``?

La solución es añadir espacios de nombres a su URLconf. En el archivo polls/urls.py, añada un app_name para configurar el espacio de nombres de la aplicación:

* polls/urls.py

    ```python
    from django.urls import path

    from . import views

    app_name = "polls"
    urlpatterns = [
        path("", views.index, name="index"),
        path("<int:question_id>/", views.detail, name="detail"),
        path("<int:question_id>/results/", views.results, name="results"),
        path("<int:question_id>/vote/", views.vote, name="vote"),
    ]
    ```

Ahora modifique su plantilla `polls/index.html` desde:

polls/templates/polls/index.html
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

para señalar la vista de detalle con espacio de nombres:

polls/templates/polls/index.html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>