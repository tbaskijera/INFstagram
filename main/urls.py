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
    path('profile/', views.profile, name='profile'),
    path('newpost/', views.NewPost, name='newpost'),
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('<int:o_id>/like', views.like, name='postlike'),
    path('<int:o_id>/comm', views.home_view, name='postcomm'),


    #path('a', PostListView.as_view(), name='homes'),
    #path('blog/<int:pk>', PostDetailView.as_view(), name='post_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)