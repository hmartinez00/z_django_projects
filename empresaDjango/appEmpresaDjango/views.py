from django.shortcuts import render
from django.http import HttpResponse
from .models import Departamento, Empleado, Habilidad

# Create your views here.

def index(request):
    return HttpResponse('Vista simple index.')

def detail(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    return HttpResponse(departamento)

def empleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    context = {
        'title_template': 'Detalles del empleado',
        'empleado': empleado,
    }
    return render(request, 'empleado.html', context)

def departamentos(request):
    departamentos = Departamento.objects.order_by('nombre') #Aca es donde esta el esquema de modelo-template-views.
    # Se usa el modelo diseñado como un objeto y se interactua con ese objeto en el
    # archivo de vistas. Se explota aqui en este archivo, y luego se arman las respuestas Http.
        
    context = {
        'title_template': 'Listado de departamentos',
        'lista_departamentos': departamentos,
    }
    return render(request, 'departamento.html', context)


