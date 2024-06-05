from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Produkty.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('kategoria/<int:id>/', kategoria, name='kategoria'),
    path('produkt/<int:id>/', produkt, name='produkt'),
    path('produkty/', lista_produktow, name='lista_produktow'),
    path('zamowienie/', zamowienie, name='zamowienie'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
