from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    # modelos = ', '.join(apps.get_models())
    return HttpResponse('Vista de Prueba!')

def index(request):
    clases = ['Clase1', 'Clase2']
    context = {
        'view_name': 'inicio',
        'title_template': 'Listado de Clases',
        'lista_clases': clases,
    }
    return render(request, 'index.html', context)
