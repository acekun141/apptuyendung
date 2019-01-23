from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
]