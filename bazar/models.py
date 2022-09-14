from pydoc import describe
from django.db import models

class Bazar(models.Model):
    titulo = models.CharField(max_length=255)
    data = models.DateField()
    total_participantes = models.DecimalField(default= 50, max_digits= 2 , decimal_places= 0)

    def __str__(self):  
        return self.titulo 
