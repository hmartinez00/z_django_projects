from django import forms

class EmpleadoForm(forms.Forms):
    nombre = forms.CharField(label = 'Nombre', max_length=100)
    apellido = forms.CharField(label = 'Apellido', max_length=100)
    edad = forms.IntegerField(label = 'Edad')
    email = forms.EmailField(label = 'Email', required=False)
    direccion = forms.CharField(label = 'Direccion', required=False)

