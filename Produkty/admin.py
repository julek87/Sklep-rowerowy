from django.contrib import admin
from .models import Produkty, Marka, Kategoria

# Register your models here.
admin.site.register(Produkty)
admin.site.register(Marka)
admin.site.register(Kategoria)
