from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Osoba, Projekt

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ('prijmeni', 'jmeno', 'email', 'pozice') # Sloupce v administraci

@admin.register(Projekt)
class ProjektAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'start_date', 'end_date', 'stav') # Sloupce v administraci
