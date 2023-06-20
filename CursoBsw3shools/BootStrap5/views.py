from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial_de_Bootstrap_5, Bootstrap_5_formularios, Rejilla_Bootstrap_5, Bootstrap_5_Otros, Certificacion


# Create your views here.

def test(request):
    return HttpResponse('Vista de Prueba!')

def index(request):
    modules = {
        'Tutorial_de_Bootstrap_5'   : [str(i).split(',')[0].split('=')[1] for i in list(Tutorial_de_Bootstrap_5.objects.order_by('id')) ],
        'Bootstrap_5_formularios'   : [str(i).split(',')[0].split('=')[1] for i in list(Bootstrap_5_formularios.objects.order_by('id')) ],
        'Rejilla_Bootstrap_5'       : [str(i).split(',')[0].split('=')[1] for i in list(Rejilla_Bootstrap_5.objects.order_by('id'))     ],
        'Bootstrap_5_Otros'         : [str(i).split(',')[0].split('=')[1] for i in list(Bootstrap_5_Otros.objects.order_by('id'))       ],
        'Certificacion'             : [str(i).split(',')[0].split('=')[1] for i in list(Certificacion.objects.order_by('id'))           ],
    }
    context = {
        'view_name'     : 'Inicio',
        'title_template': 'Listado de Clases',
        'modules'       : modules,
    }
    return render(request, 'index.html', context)



def vistas_clases(request):
    context = {}
    return render(request, 'bs5_empezar.html', context)
