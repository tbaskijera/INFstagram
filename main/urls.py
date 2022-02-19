from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('registration', views.registration, name='register'),
    path('login', views.login, name='login')
]