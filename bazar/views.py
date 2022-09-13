from django.shortcuts import render
from django.views.generic import ListView
from .models import Bazar

class BazarListView(ListView):
    model = Bazar

