from django.shortcuts import render
from django.views.generic import ListView
from .models import Participante 

class ParticipanteListView(ListView):
    model = Participante
