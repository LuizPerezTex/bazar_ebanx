from django.urls import path 
from .views import BazarListView


urlpatterns = [
    path('', BazarListView.as_view(), name='organizador'),
]