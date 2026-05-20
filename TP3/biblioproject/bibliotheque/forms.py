from django.forms import ModelForm
from . import models

class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('nom', 'descriptif')

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'date_depart', 'nb_page', 'resume', 'auteur', 'categorie')