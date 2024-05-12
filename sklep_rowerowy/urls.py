from django.contrib import admin
from django.urls import path
from Produkty.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('kategoria/<int:id>/', kategoria, name='kategoria'),
    path('produkt/<int:id>/', produkt, name='produkt')
]
