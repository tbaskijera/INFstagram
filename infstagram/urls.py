"""infstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as views_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    
    
    
    
    path('homepage', views_main.homepage, name='homepage'),
    path('registration', views_main.register_user, name='register'),
    path('login', views_main.login_user, name='login'),
    path('changepassword/', views_main.password_change, name='change_password'),
   	path('changepassword/done', views_main.password_change_done, name='change_password_done'),
    path('updateprofile', views_main.edit_profile, name='updateprofile'),
    path('logout', views_main.logout_view, name='logout'),
    path('profile', views_main.profil, name='profile'),
    path('profile/newpost/', views_main.NewPost, name='newpost'),
    path('home', views_main.home, name='home'),
    # dode greska u testu jer se zove isto ko ovaj gore p je dodano redirect
    path('', views_main.redirect_view, name='home_redirect'),
    path('<int:post_id>/like', views_main.like, name='postlike'),
    path('<int:post_id>/comm', views_main.comment, name='postcomm'),
    path('<int:k_id>/deletecomm', views_main.delete_comment, name='deletecomm')
]
