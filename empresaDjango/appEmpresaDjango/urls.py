from django.urls import path
from . import views

urlpatterns = [
	path('departamentos/', views.departamentos, name='departamentos'),
	path('empleado/<int:empleado_id>', views.empleado, name='empleado'),
	path('detail/<int:departamento_id>', views.detail, name='detail'),
	path('', views.index, name='index'),
]
