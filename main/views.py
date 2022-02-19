from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('<html><body><h1>POCETAK INFSTAGRAM</h1></body></html>')