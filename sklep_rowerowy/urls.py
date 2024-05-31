from django.contrib import admin
from django.urls import path, include
from Produkty.views import *
from Produkty import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kategoria/<int:id>/', kategoria, name='kategoria'),
    path('produkt/<int:id>/', produkt, name='produkt'),
    path('dodaj/', dodaj_produkt, name='dodaj_produkt'),
    path('koszyk/', views.koszyk, name='koszyk'),
    path('dodaj_do_koszyka/<int:produkt_id>/', views.dodaj_do_koszyka, name='dodaj_do_koszyka'),
]

