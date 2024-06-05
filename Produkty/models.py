from django.db import models
from django.contrib.auth.models import User

class Marka(models.Model):
    def __str__(self):
        return self.marka

    marka = models.CharField(max_length=50, null=True, blank=False)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Marki"

class Kategoria(models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Produkty(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, null=True)
    kategoria = models.ForeignKey(Kategoria, null=True, blank=True, on_delete=models.CASCADE, )
    model = models.CharField(max_length=50, null=True, blank=False)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    rezerwacja = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marka} {self.model}"

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

class Koszyk(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class PozycjaKoszyka(models.Model):
    koszyk = models.ForeignKey(Koszyk, on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField(default=1)

class Zamowienie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='zamowienia')
    created_at = models.DateTimeField(auto_now_add=True)

class PozycjaZamowienia(models.Model):
    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE, related_name='pozycje')
    produkt = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    ilosc = models.PositiveIntegerField(default=1)
