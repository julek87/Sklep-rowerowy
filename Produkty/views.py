from django.shortcuts import render, redirect
from .models import Produkty, Kategoria, Koszyk, PozycjaKoszyka
from .forms import DodajProduktForm
from django.contrib.auth.decorators import login_required


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


def dodaj_produkt(request):
    if request.method == 'POST':
        form = DodajProduktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DodajProduktForm()
    return render(request, 'dodaj_produkt.html', {'form': form})


def dodaj_do_koszyka(request, produkt_id):
    if request.user.is_authenticated:
        produkt = Produkty.objects.get(pk=produkt_id)
        koszyk, created = Koszyk.objects.get_or_create(user=request.user)
        pozycja, created = PozycjaKoszyka.objects.get_or_create(koszyk=koszyk, produkt=produkt)
        if not created:
            pozycja.ilosc += 1
            pozycja.save()
        return render(request, 'dodaj do koszyka.html', {'produkt': produkt})
    else:
        return render(request, 'brak_dostepu.html')

@login_required
def koszyk(request):
    koszyk, created = Koszyk.objects.get_or_create(user=request.user)
    pozycje = koszyk.pozycjakoszyka_set.all()
    context = {'koszyk': koszyk, 'pozycje': pozycje}
    return render(request, 'koszyk.html', context)