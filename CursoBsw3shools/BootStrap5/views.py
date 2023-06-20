from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial_de_Bootstrap_5, Bootstrap_5_formularios, Rejilla_Bootstrap_5, Bootstrap_5_Otros, Certificacion


# Create your views here.

def test(request):
    # modelos = ', '.join(apps.get_models())
    return HttpResponse('Vista de Prueba!')

def index(request):
    clases_Tutorial_de_Bootstrap_5 = [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id'))]
    Modulos = {
        'Tutorial_de_Bootstrap_5': [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id'))],
        'Bootstrap_5_formularios': [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id'))],
        'Rejilla_Bootstrap_5': [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id'))],
        'Bootstrap_5_Otros': [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id'))],
        'Certificacion': [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id'))],
    }
    module_name = list(Modulos.keys())[0]
    class_list = Modulos[module_name]
    context = {
        'view_name': 'inicio',
        'title_template': 'Listado de Clases',
        'module_name': module_name,
        'class_list': class_list,
    }
    return render(request, 'index.html', context)
