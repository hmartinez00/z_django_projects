from django.urls import path
from . import views

urlpatterns = [
	path('vistas_clases/<str:modulo>/<str:clase>', views.vistas_clases, name='vistas_clases'),
	path('test/', views.test, name='test'),
	path('', views.index, name='index'),
]