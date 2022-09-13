from pydoc import describe
from django.db import models

class Bazar(models.Model):
    titulo = models.CharField(max_length=255)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):  
        return self.titulo
