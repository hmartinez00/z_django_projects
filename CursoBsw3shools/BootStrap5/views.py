from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    # modelos = ', '.join(apps.get_models())
    return HttpResponse('Vista de Prueba!')

def index(request):
    clases = [
        'BS5_INICIO',
        'BS5_Empezar',
        'Contenedores_BS5',
        'BS5_Rejilla_Básica',
        'Tipografía_BS5',
        'Colores_BS5',
        'Tablas_BS5',
        'Imágenes_BS5',
        'Jumbotrón_BS5',
        'Alertas_BS5',
        'Botones_BS5',
        'Grupos_de_botones_BS5',
        'Insignias_BS5',
        'Barras_de_progreso_BS5',
        'Hilanderos_BS5',
        'Paginación_BS5',
        'Grupos_de_listas_BS5',
        'Tarjetas_BS5',
        'Menús_desplegables_BS5',
        'BS5_Colapso',
        'Navegadores_BS5',
        'Barra_de_navegación_BS5',
        'Carrusel_BS5',
        'Modalidad_BS5',
        'Información_sobre_herramientas_BS5',
        'Ventana_emergente_BS5',
        'Tostadas_BS5',
        'BS5_Scrollspy',
        'BS5_Offcanvas',
        'Utilidades_BS5',
        'Flexibilidad_BS5',
    ]
    context = {
        'view_name': 'inicio',
        'title_template': 'Listado de Clases',
        'lista_clases': clases,
    }
    return render(request, 'index.html', context)
