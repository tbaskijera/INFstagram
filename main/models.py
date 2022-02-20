from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#ovo se ne koristi i dalje msm ovaj model
class Korisnik(models.Model):
    
    ime = models.CharField(max_length = 30)
    prezime = models.CharField(max_length = 70)
    datum_rodenja = models.DateField()

    def __str__(self):
        return self.prezime
    

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length = 120, null=True)
    slika_profil = models.ImageField(upload_to='profile_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.slika_profil.path)
        if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.slika_profil.path)

    def __str__(self):
        return self.user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profil.save()


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