from django.contrib import admin
from .models import *

# Register your models here.



model_list = [Korisnik, Profil, Objava, Komentar]
admin.site.register(model_list)

