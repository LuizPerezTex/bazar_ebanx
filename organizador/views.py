from django.shortcuts import render
from django.views.generic import ListView
from .models import Organizador

class OrganizadorListView(ListView):
    model = Organizador
