from django.db import models

class TableData(models.Model):
    name = models.CharField(max_length=255)
    value = models.IntegerField()
