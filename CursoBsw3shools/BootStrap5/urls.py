from django.urls import path
from . import views

urlpatterns = [
	path('example/<str:modulo>/<str:leccion>/<int:num_id>', views.example, name='example'),
	path('vistas_clases/<str:modulo>/<str:leccion>', views.vistas_clases, name='vistas_clases'),
	path('test/', views.test, name='test'),
	path('', views.index, name='index'),
]
