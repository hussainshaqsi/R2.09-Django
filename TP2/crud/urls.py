from django.urls import path
from . import views

urlpatterns = [
    path('', views.all),                              # /bibliotheque/  → list
    path('ajout/', views.ajout),                      # show create form
    path('traitement/', views.traitement),            # process create
    path('affiche/<int:id>/', views.read),            # show one book
    path('update/<int:id>/', views.update),           # show update form
    path('traitementupdate/<int:id>/', views.traitementupdate),  # process update
    path('delete/<int:id>/', views.delete),           # delete
]
