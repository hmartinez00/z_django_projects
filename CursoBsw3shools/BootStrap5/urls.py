from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	path('vistas_clases/<str:modulo>/<str:leccion>/<int:num>', views.vistas_clases, name='vistas_clases'),
	path('test/', views.test, name='test'),
	path('', views.index, name='index'),
]
