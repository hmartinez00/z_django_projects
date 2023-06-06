from django.urls import path
from . import views

urlpatterns = [
	path('departamento/<int:departamento_id>', views.departamento, name='departamento'),
	path('', views.index, name='index'),
]
