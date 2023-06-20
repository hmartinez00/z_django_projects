from django.db import models

# Create your models here.

class Tutorial_de_Bootstrap_5(models.Model):
    content         = models.CharField(max_length=100)
    time            = models.IntegerField(default=1)
    youtube_url     = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content}, time={self.time}, youtube_url={self.youtube_url} '
        return out

class Bootstrap_5_formularios(models.Model):
    content         = models.CharField(max_length=100)
    time            = models.IntegerField(default=1)
    youtube_url     = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content}, time={self.time}, youtube_url={self.youtube_url} '
        return out

class Rejilla_Bootstrap_5(models.Model):
    content         = models.CharField(max_length=100)
    time            = models.IntegerField(default=1)
    youtube_url     = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content}, time={self.time}, youtube_url={self.youtube_url} '
        return out

class Bootstrap_5_Otros(models.Model):
    content         = models.CharField(max_length=100)
    time            = models.IntegerField(default=1)
    youtube_url     = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content}, time={self.time}, youtube_url={self.youtube_url} '
        return out

class Certificacion(models.Model):
    content         = models.CharField(max_length=100)
    time            = models.IntegerField(default=1)
    youtube_url     = models.CharField(max_length=100)

    def __str__(self):
        out = f'content={self.content}, time={self.time}, youtube_url={self.youtube_url} '
        return out
