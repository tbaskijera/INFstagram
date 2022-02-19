from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *


# Create your views here.
def registracija(response):
    if response.user.is_authenticated:
        logout(response)

    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            print("Uspjesno")
        return redirect("/")
    else:
        form = UserCreationForm()

    return render(response, "register.html", {"form": form})


def prijava(request):
    return render(request, "log_in.html")