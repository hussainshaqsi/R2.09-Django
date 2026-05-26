from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .forms import CategorieForm, LivreForm
from . import models
# Create your views here.
# ===== CATEGORIE CRUD =====

def skelete(request):
    return render(request,"bibliotheque/home.html") #views needs to call the infant and not the child


def categorie_index(request):
    categories = models.Categorie.objects.all()
    return render(request, "bibliotheque/categorie_index.html", {"categories": categories})

def categorie_ajout(request):
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bibliotheque/categories/")
        return render(request, "bibliotheque/categorie_form.html", {"form": form})
    return render(request, "bibliotheque/categorie_form.html", {"form": CategorieForm()})

def categorie_read(request, id):
    categorie = get_object_or_404(models.Categorie, pk=id)
    return render(request, "bibliotheque/categorie_detail.html", {"categorie": categorie})

def categorie_update(request, id):
    categorie = get_object_or_404(models.Categorie, pk=id)
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id = id
            obj.save()
            return HttpResponseRedirect("/bibliotheque/categories/")
        return render(request, "bibliotheque/categorie_form.html", {"form": form, "id": id})
    form = CategorieForm(instance=categorie)
    return render(request, "bibliotheque/categorie_form.html", {"form": form, "id": id})

def categorie_delete(request, id):
    categorie = get_object_or_404(models.Categorie, pk=id)
    categorie.delete()
    return HttpResponseRedirect("/bibliotheque/categories/")

# ===== LIVRE CRUD =====

def livre_index(request):
    livres = models.Livre.objects.all()
    return render(request, "bibliotheque/livre_index.html", {"livres": livres})

def livre_ajout(request):
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/bibliotheque/livres/")
        return render(request, "bibliotheque/livre_form.html", {"form": form})
    return render(request, "bibliotheque/livre_form.html", {"form": LivreForm()})

def livre_read(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    return render(request, "bibliotheque/livre_detail.html", {"livre": livre})

def livre_update(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    if request.method == "POST":
        form = LivreForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id = id
            obj.save()
            return HttpResponseRedirect("/bibliotheque/livres/")
        return render(request, "bibliotheque/livre_form.html", {"form": form, "id": id})
    form = LivreForm(instance=livre)
    return render(request, "bibliotheque/livre_form.html", {"form": form, "id": id})

def livre_delete(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    livre.delete()
    return HttpResponseRedirect("/bibliotheque/livres/")

# ===== HOME =====
def home(request):
    return render(request, "bibliotheque/home.html")