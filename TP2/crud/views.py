from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LivreForm
from . import models


# CREATE - show the empty form
def ajout(request):
    form = LivreForm()
    return render(request, "crud/ajout.html", {"form": form})


# CREATE - process the submitted form
def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request, "crud/affiche.html", {"Livre": livre})
    else:
        return render(request, "crud/ajout.html", {"form": lform})


# READ - one book by id
def read(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request, "crud/affiche.html", {"Livre": livre})


# ALL - list every book
def all(request):
    livres = list(models.Livre.objects.all())
    return render(request, "crud/all.html", {"livres": livres})


# UPDATE - show the form pre-filled
def update(request, id):
    livre = models.Livre.objects.get(pk=id)
    dictionnaire = {
        'titre': livre.titre,
        'auteur': livre.auteur,
        'date_parution': livre.date_parution,
        'nombre_pages': livre.nombre_pages,
        'resume': livre.resume,
    }
    lform = LivreForm(dictionnaire)
    return render(request, "crud/update.html", {"form": lform, "id": id})


# UPDATE - process the modified form
def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save(commit=False)  # don't save to DB yet
        livre.id = id                      # force the existing id
        livre.save()                       # now save (= UPDATE, not INSERT)
        return HttpResponseRedirect("/bibliotheque/")
    else:
        return render(request, "crud/update.html", {"form": lform, "id": id})


# DELETE
def delete(request, id):
    livre = models.Livre.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/")