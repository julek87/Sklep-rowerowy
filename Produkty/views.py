from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produkty, Koszyk, PozycjaKoszyka, Zamowienie, PozycjaZamowienia, Kategoria

def index(request):
    kategorie = Kategoria.objects.all()
    produkty = Produkty.objects.all()
    return render(request, 'index.html', {'kategorie': kategorie, 'produkty': produkty})

def kategoria(request, id):
    kategorie = Kategoria.objects.all()
    produkty = Produkty.objects.filter(kategoria_id=id)
    return render(request, 'index.html', {'kategorie': kategorie, 'produkty': produkty})

def produkt(request, id):
    produkt = Produkty.objects.get(id=id)
    return render(request, 'szczegoly_produktu.html', {'produkt': produkt})

def lista_produktow(request):
    produkty = Produkty.objects.all()
    return render(request, 'lista_produktow.html', {'produkty': produkty})

@login_required
def zamowienie(request):
    koszyk = Koszyk.objects.get(user=request.user)
    zamowienie = Zamowienie.objects.create(user=request.user)
    for pozycja in koszyk.pozycjakoszyka_set.all():
        PozycjaZamowienia.objects.create(
            zamowienie=zamowienie,
            produkt=pozycja.produkt,
            ilosc=pozycja.ilosc
        )
    koszyk.pozycjakoszyka_set.all().delete()
    return redirect('lista_produktow')
