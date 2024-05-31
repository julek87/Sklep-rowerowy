from django import forms
from .models import Produkty

class DodajProduktForm(forms.ModelForm):
    class Meta:
        model = Produkty
        fields = ['marka', 'model', 'rezerwacja']
