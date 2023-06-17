from django.shortcuts import render
from django.http import HttpResponse

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
    
