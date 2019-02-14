from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import InfomationEnterprise, Post
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
        signin = self.client.get(reverse('signin'))
        signup = self.client.get(reverse('signup'))
        post = self.client.get(reverse('post'))
        infoform = self.client.get(reverse('infoform'))
        listpost = self.client.get(reverse('listpost'))
        self.assertEqual(homepage.status_code, 200)
        self.assertEqual(signin.status_code, 200)
        self.assertEqual(signup.status_code, 200)
        self.assertEqual(post.status_code, 302)
        self.assertEqual(infoform.status_code, 302)
        self.assertEqual(listpost.status_code, 302)
class TestInfo(TestCase):
    def setUp(self):
        InfomationEnterprise.objects.create(company = "name_of_company", describe="describe_of_company")
    
    def test_describe(self):
        info = InfomationEnterprise.objects.get(id = 1)
        expected_describe = f'{info.describe}'
        self.assertEqual(expected_describe, 'describe_of_company')


class TestPost(TestCase):
    def setUp(self):
        InfomationEnterprise.objects.create(username = 'username1')
        info = InfomationEnterprise.objects.get(username = 'username1')
        info.post_set.create(title = 'title of username1')
    def test_title(self):
        post = Post.objects.get(id = 1)
        expected_title = f'{post.title}'
        self.assertEqual(expected_title, 'title of usernamex')


    
