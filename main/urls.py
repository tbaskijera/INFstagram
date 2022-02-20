from django.urls import path
from . import views
from django.contrib.auth import views as authViews 

app_name = 'main'

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('registration', views.registration, name='register'),
    path('login', views.loginuser, name='login'),
    path('changepassword/', views.PasswordChange, name='change_password'),
   	path('changepassword/done', views.PasswordChangeDone, name='change_password_done'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
]