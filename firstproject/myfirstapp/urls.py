
from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index),
    path('formulaire/', views.formulaire, name='formulaire'),
]