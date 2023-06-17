from django.urls import path
from . import views

urlpatterns = [
	path('post_empleado_form/', views.post_empleado_form, name='post_empleado_form'),
	path('empleado/', views.show_empleado_form, name='empleado'),
	path('registrar/', views.registrar, name='registrar'),
	path('registro/', views.registro, name='registro'),
]
