from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
from . import views
class TestPage(SimpleTestCase):
    def test_all_page_status_code(self):
        homepage = self.client.get("/")
        signin = self.client.get("/signin/")
        signup = self.client.get("/signup/")
        post = self.client.get("/post/")
        infoform = self.client.get("/infoform/")
        listpost = self.client.get("/listpost/")
        self.assertEqual(homepage.status_code,200)
        self.assertEqual(signin.status_code,200)
        self.assertEqual(signup.status_code,200)
        self.assertEqual(post.status_code, 302)
        self.assertEqual(infoform.status_code, 302)
        self.assertEqual(listpost.status_code, 302)
    def test_view_url_by_name(self):
        homepage = self.client.get(reverse('home'))
        signin = self.client.get(reverse('singin'))
        signup = self.client.get(reverse('signup'))
        post = self.client.get(reverse('post'))
        infoform = self.client.get(reverse('infoform'))
        listpost = self.client.get(reverse('listpost'))
        self.assertEqual(homepage.status_code, 200)
        self.assertEqual(signin.status_code, 200)
        self.assertEqual(signup.status_code, 200)
        self.assertEqual(post.status_code, 302)
        self.assertEqual(infoform.status_code, 302)
        self.assertEqual(listpost.status_code, 200)
    
