from django.db import models

# Create your models here.

class Tutorial_de_Bootstrap_5(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content} '
        return out

class Bootstrap_5_formularios(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content} '
        return out

class Rejilla_Bootstrap_5(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content} '
        return out

class Bootstrap_5_Otros(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content} '
        return out

class Certificacion(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content} '
        return out
