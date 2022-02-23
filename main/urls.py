from django.urls import path
from . import views
from django.contrib.auth import views as authViews 
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
#from .views import PostListView, PostDetailView
urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('registration', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('changepassword/', views.password_change, name='change_password'),
   	path('changepassword/done', views.password_change_done, name='change_password_done'),
    path('updateprofile', views.edit_profile, name='updateprofile'),
    path('logout', views.logout_view,name='logout'),
    path('profile', views.profil, name='profile'),
    path('profile/newpost/', views.NewPost, name='newpost'),
    path('home', views.home, name='home'),
    path('', views.redirect_view, name='home'),
    path('<int:post_id>/like', views.like, name='postlike'),
    path('<int:post_id>/comm', views.comment, name='postcomm'),
    path('<int:k_id>/deletecomm', views.delete_comment, name='deletecomm')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)