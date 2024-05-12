from django.http import HttpResponse
from django.shortcuts import render
from .models import Produkty, Kategoria


def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategorie_rowery = Produkty.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
                 'kategorie_rowery': kategorie_rowery,
                 'kategorie': kategorie}
    return render(request, 'kategorie_rowery.html', dane)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    tekst = {'produkt_user': produkt_user}
    return render(request, 'produkt.html', tekst)
