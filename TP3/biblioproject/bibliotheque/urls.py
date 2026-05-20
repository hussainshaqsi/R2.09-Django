from django.urls import path, include
from . import views
urlpatterns = [ path('', views.home),

    # Categories
    path('categories/', views.categorie_index),
    path('categories/ajout/', views.categorie_ajout),
    path('categories/<int:id>/', views.categorie_read),
    path('categories/<int:id>/update/', views.categorie_update),
    path('categories/<int:id>/delete/', views.categorie_delete),

    # Livres
    path('livres/', views.livre_index),
    path('livres/ajout/', views.livre_ajout),
    path('livres/<int:id>/', views.livre_read),
    path('livres/<int:id>/update/', views.livre_update),
    path('livres/<int:id>/delete/', views.livre_delete),]  # we'll fill this as we go