from pyexpat import model
from django.db import models

class Participante(models.Model):
    nome_usuario = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nome_usuario
