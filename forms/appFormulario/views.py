from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmpleadoForm

# Create your views here.

def registro(request):
    return render(request, 'registro.html')

def registrar(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    edad = request.POST['edad']
    email = request.POST['email']
    direccion = request.POST['direccion']

    out = f'{nombre} -- {apellido} -- {edad} -- {email} -- {direccion}'

    return HttpResponse(out)
    

def show_empleado_form(request):
    form = EmpleadoForm()
    context = {'form': form}
    return render(request, 'empleado_form.html', context)


def post_empleado_form(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        out = f'El nombre es: {nombre}'
        return HttpResponse(out)

