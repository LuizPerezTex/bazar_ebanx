import email
from django.db import models

class Organizador(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
