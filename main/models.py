from email.policy import default
#from tkinter import CASCADE
from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import django.utils.timezone

# Create your models here.

#ovo se ne koristi i dalje msm ovaj model
class Korisnik(models.Model):
    
    ime = models.CharField(max_length = 30)
    prezime = models.CharField(max_length = 70)
    datum_rodenja = models.DateField()

    def __str__(self):
        return self.prezime
    

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    bio = models.CharField(max_length = 120, null=True)
    slika_profil = models.ImageField(upload_to='static/image', default='static/image/default_avatar.png')

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
    profil_objava = models.ForeignKey(Profil, on_delete = models.CASCADE)
    #profil_objava = models.ForeignKey(User, on_delete=models.CASCADE)
    slika_objava = models.ImageField(upload_to='static/image')
    opis_objava = models.CharField(max_length = 500)
    vrijeme_objava = models.DateTimeField(null=True)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.slika_objava.path)
        if img.mode in ("RGBA", "P"): img = img.convert("RGB")
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.slika_objava.path)
    
    def __str__(self):
        return self.opis_objava

class Likes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
	post = models.ForeignKey(Objava, on_delete=models.CASCADE, related_name='post_like')

class Komentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comm')
    post = models.ForeignKey(Objava, on_delete=models.CASCADE, related_name='post_comm')
    comment = models.CharField(max_length=400)
    title = models.CharField(max_length=100, default='a')
    #created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:60]