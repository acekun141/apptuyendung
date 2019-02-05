from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/', views.post_view, name='post'),
    path('signin/', views.signin_view, name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name="logout"),
    path('infoform/', views.infoform, name='infoform'),
    path('listpost/', views.listpost, name="listpost"),
    path('newfeed/', views.newfeed, name="newfeed"),
    path('post/<int:id>/', views.post, name='singlepost'),
]