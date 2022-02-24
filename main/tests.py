from django.urls import reverse, resolve
from django.http import HttpRequest
from django.test import TestCase
from matplotlib import use
from .models import *
from .views import *
from django.contrib.auth.models import User

# Create your tests here.

class Testovi(TestCase):

    def test_homepage(self):
        request = HttpRequest() 
        response = homepage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<body><h1>POCETAK INFSTAGRAM</h1></body>', response.content) 
        self.assertTrue(response.content.endswith(b'</html>'))
    
    def test_registration(self):
        path = reverse("register")
        self.assertEqual(resolve(path).func, register_user)
    
    def test_login(self):
        path = reverse("login")
        self.assertEqual(resolve(path).func, login_user)

    def test_changepassword(self):
        path = reverse("change_password")
        self.assertEqual(resolve(path).func, password_change)

    def test_changepassword_done(self):
        path = reverse("change_password_done")
        self.assertEqual(resolve(path).func, password_change_done)
    
    def test_updateprofile(self):
        path = reverse("updateprofile")
        self.assertEqual(resolve(path).func, edit_profile)

    def test_logout(self):
        path = reverse("logout")
        self.assertEqual(resolve(path).func, logout_view)

    def test_profile(self):
        path = reverse("profile")
        self.assertEqual(resolve(path).func, profil)

    def test_newpost(self):
        path = reverse("newpost")
        self.assertEqual(resolve(path).func, NewPost)

    def test_home(self):
        path = reverse("home")
        self.assertEqual(resolve(path).func, home)

    def test_redirect(self):
        path = reverse("home_redirect")
        self.assertEqual(resolve(path).func, redirect_view)
    
    def test_like(self):
        path = reverse("postlike", args=[2])
        self.assertEqual(resolve(path).func, like)

    def test_comment(self):
        path = reverse("postcomm", args=[3])
        self.assertEqual(resolve(path).func, comment)

    def test_celetecomment(self):
        path = reverse("deletecomm", args=[1])
        self.assertEqual(resolve(path).func, delete_comment)

# from datetime import datetime
# class TestComment(TestCase):
#     def setUp(self):
#         user1 = User.objects.create_user('Chevy Chase', 'chevy@chase.com', 'chevyspassword')
#         self.likes = Profile.objects.create(
#             user_id = user1,
#             bio = "bio",
#             profile_image='static/image/default_avatar.png'
#         )

#     def testLikes(self):
#         self.assertEquals(self.likes.bio, 'bio')


class ModelTest(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user('Testni User', 'test@gmail.com', 'testpassword')

    def testUser(self):
        self.assertCountEqual(self.user_1.email, 'test@gmail.com')


