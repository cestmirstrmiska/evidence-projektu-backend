from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Osoba(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=100, verbose_name="Příjmení")
    # Zajištění unikátnosti e-mailu na úrovni DB
    email = models.EmailField(unique=True, verbose_name="Email")
    pozice = models.CharField(max_length=100, verbose_name="Pracovní Pozice")

    def __str__(self):
        return f"{self.prijmeni} {self.jmeno}"

class Projekt(models.Model):
    # Zajištění unikátnosti názvu projektu na úrovni DB
    nazev = models.CharField(max_length=200, unique=True, verbose_name="Název projektu")
    popis = models.TextField(blank=True, verbose_name="Popis")
    start_date = models.DateField(verbose_name="Datum zahájení")
    end_date = models.DateField(null=True, blank=True, verbose_name="Datum ukončení")
    stav = models.CharField(max_length=50, verbose_name="Stav projektu")
    clenove = models.ManyToManyField(Osoba, related_name="projekty", verbose_name="Členové týmu")

    # LOGICKÁ VALIDACE DATUMŮ NA ÚROVNI DJANGA
    def clean(self):
        super().clean()
        # Kontrola, zda jsou vyplněna obě data a zda konec nepředchází začátek
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise ValidationError({
                    'end_date': "Datum ukončení projektu nemůže nastat dříve než datum jeho zahájení."
                })

    def __str__(self):
        return self.nazev
