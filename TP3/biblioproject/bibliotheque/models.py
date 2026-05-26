from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    date_depart = models.DateField(blank=True, null=True)
    nb_page = models.IntegerField()
    resume = models.TextField(blank=True, null=True)
    auteur = models.CharField(max_length=100)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name='livres'
    )
    Image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return f"{self.titre} ({self.categorie})"


