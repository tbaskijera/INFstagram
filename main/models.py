from django.db import models
from PIL import Image
import os
from django.conf import settings

# Create your models here.

class Korisnik(models.Model):
    ime = models.CharField(max_length = 30)
    prezime = models.CharField(max_length = 70)
    datum_rodenja = models.DateField()

    def __str__(self):
        return self.prezime
    

class Profil(models.Model):
    korisnicko_ime = models.CharField(max_length = 20)
    lozinka = models.CharField(max_length= 30)
    bio = models.CharField(max_length = 120)
    slika_profil = models.ImageField()
    korisnik = models.ForeignKey("Korisnik", on_delete = models.CASCADE)

    def __str__(self):
        return self.korisnicko_ime


class Objava(models.Model):
    profil_objava = models.ForeignKey("Profil", on_delete = models.CASCADE)
    slika_objava = models.ImageField()
    opis_objava = models.CharField(max_length = 500)
    vrijeme_objava = models.DateTimeField()
    lajk_objava = models.IntegerField()
    
    def __str__(self):
        return self.opis_objava


class Komentar(models.Model):
    profil_komentar = models.ForeignKey("Profil", on_delete = models.CASCADE)
    opis_komentar = models.CharField(max_length = 500)
    objava_komentar = models.ForeignKey("Objava", on_delete = models.CASCADE)
    vrijeme_komentar = models.DateTimeField()
    lajk_komentar = models.IntegerField()

    def __str__(self):
        return self.opis_komentar