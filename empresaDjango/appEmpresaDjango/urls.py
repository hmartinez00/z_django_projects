from django.urls import path
from . import views

urlpatterns = [
	path('departamento/', views.departamento, name='departamento'),
	path('', views.index, name='index'),
]
