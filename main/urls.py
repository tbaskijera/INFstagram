from django.urls import path
from . import views
from django.contrib.auth import views as authViews 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
#from .views import PostListView, PostDetailView
urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('registration', views.registration, name='register'),
    path('login', views.loginuser, name='login'),
    path('changepassword/', views.PasswordChange, name='change_password'),
   	path('changepassword/done', views.PasswordChangeDone, name='change_password_done'),
    path('updateprofile', views.update_profile, name='updateprofile'),
    path('logout', views.logout_view,name='logout'),
    path('profil/', views.profil, name='profil'),
    path('newpost/', views.NewPost, name='newpost'),
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('<int:o_id>/like', views.like, name='postlike'),
    path('<int:o_id>/comm', views.home_view, name='postcomm'),


    #path('a', PostListView.as_view(), name='homes'),
    #path('blog/<int:pk>', PostDetailView.as_view(), name='post_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)