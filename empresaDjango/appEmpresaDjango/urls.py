from django.urls import path
from . import views

urlpatterns = [
	path('empleados/', views.empleados, name='empleados'),
	path('empleado/<int:empleado_id>', views.empleado, name='empleado'),
	path('departamentos/', views.departamentos, name='departamentos'),
	path('departamento/<int:departamento_id>', views.departamento, name='departamento'),
	path('', views.index, name='index'),
	path('test', views.test, name='test'),
]
