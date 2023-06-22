import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial_de_Bootstrap_5, Bootstrap_5_formularios, Rejilla_Bootstrap_5, Bootstrap_5_Otros, Certificacion
from CursoBsw3shools.settings import TEMPLATES


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

def vistas_clases(request, modulo, leccion):
    template_name   = os.path.join(modulo, leccion, leccion + '.html')
    template_dir    = os.path.join(TEMPLATES[0]['DIRS'][0], modulo, leccion)
    file_list       = [i for i in os.listdir(template_dir) if i != leccion + '.html']
    context = {
        'modulo'    : modulo,
        'leccion'   : leccion,
        'file_list' : file_list,
    }
    return render(request, template_name, context)

def example(request, modulo, leccion, num_id):
    template_name = os.path.join(modulo, leccion, f'example{num_id}.html')
    context = {
        'modulo'    : modulo,
        'leccion'   : leccion,
        'num_id'    : num_id
    }
    return render(request, template_name, context)
