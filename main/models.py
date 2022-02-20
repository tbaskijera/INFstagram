from django.db import models
from PIL import Image
import os
from django.conf import settings

def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
        full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

        if os.path.exists(full_path):
            os.remove(full_path)

        return profile_pic_name
# Create your models here.

class Korisnik(models.Model):
    ime = models.CharField(max_length = 30)
    prezime = models.CharField(max_length = 70)
    datum_rodenja = models.DateField()

    def __str__(self):
        return self.prezime
    

class Profil(models.Model):
    picture = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Picture')
    bio = models.TextField(max_length=150, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
	    
        SIZE = 250, 250

        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)


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