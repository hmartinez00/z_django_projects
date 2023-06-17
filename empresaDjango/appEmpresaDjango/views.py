from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponse
from .models import Departamento, Empleado, Habilidad


# Create your views here.

def test(request):
    # modelos = ', '.join(apps.get_models())
    return HttpResponse('Hola!')

def index(request):
    modelos = ['departamentos', 'empleados']
    context = {
        'view_name': 'inicio',
        'title_template': 'Listado de modelos',
        'lista_modelos': modelos,
    }
    return render(request, 'index.html', context)

# def departamentos(request):
#     departamentos = Departamento.objects.order_by('nombre')
#     context = {
#         'view_name': 'departamentos',
#         'title_template': 'Listado de departamentos',
#         'lista_departamentos': departamentos,
#     }
#     return render(request, 'departamentos.html', context)

class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamentos.html'
    queryset = Departamento.objects.order_by('nombre')
    # context_object_name = 'lista_departamentos'

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListView, self).get_context_data(**kwargs)
        context['title_template'] = 'Listado de departamentos'
        return context


def departamento(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    return HttpResponse(departamento)

def empleados(request):
    empleados = Empleado.objects.order_by('nombre')
    context = {
        'view_name': 'empleados',
        'title_template': 'Listado de empleados',
        'lista_empleados': empleados,
    }
    return render(request, 'empleados.html', context)

# def empleado(request, empleado_id):
#     empleado = Empleado.objects.get(pk=empleado_id)
#     context = {
#         'view_name': 'empleado',
#         'title_template': 'Detalles del empleado',
#         'empleado': empleado,
#     }
#     return render(request, 'empleado.html', context)

class EmpleadoDetailview(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailview, self).get_context_data(**kwargs)
        context['title_template'] = 'Detalles del empleado'
        return context