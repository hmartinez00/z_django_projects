from django.shortcuts import render
from django.http import HttpResponse
from .models import Departamento, Empleado, Habilidad


# Create your views here.

def test(request):
    # modelos = ', '.join(apps.get_models())
    return HttpResponse('Hola!')

def index(request):
    modelos = ['departamentos', 'empleados']
    context = {
        'title_template': 'Listado de modelos',
        'lista_modelos': modelos,
    }
    return render(request, 'index.html', context)


def departamentos(request):
    departamentos = Departamento.objects.order_by('nombre')
    context = {
        'title_template': 'Listado de departamentos',
        'lista_departamentos': departamentos,
    }
    return render(request, 'departamentos.html', context)

def departamento(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    return HttpResponse(departamento)

def empleados(request):
    empleados = Empleado.objects.order_by('nombre')
    context = {
        'title_template': 'Listado de empleados',
        'lista_empleados': empleados,
    }
    return render(request, 'empleados.html', context)

def empleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    context = {
        'title_template': 'Detalles del empleado',
        'empleado': empleado,
    }
    return render(request, 'empleado.html', context)

