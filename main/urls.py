from django.urls import path
from . import views
from django.contrib.auth import views as authViews 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('registration', views.registration, name='register'),
    path('login', views.loginuser, name='login'),
    path('changepassword/', views.PasswordChange, name='change_password'),
   	path('changepassword/done', views.PasswordChangeDone, name='change_password_done'),
    path('updateprofile', views.update_profile, name='updateprofile'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('profil/', views.profil, name='profil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)