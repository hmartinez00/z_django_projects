from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField(default=0)

    def __str__(self):
        out = f'nombre={self.nombre} , telefono={self.telefono} '
        return out

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        out = f'nombre={self.nombre} '
        return out

class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        out = f'departamento={self.departamento} , nombre={self.nombre} , fecha_nacimiento={self.fecha_nacimiento} , antiguedad={self.antiguedad} '
        return out
