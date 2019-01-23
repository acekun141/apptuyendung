from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, SigninForm
# Create your views here.
def home_view(request):
    if request.user.username:
        return HttpResponseRedirect('post/')
    return render(request, 'pages/home.html')

def post_view(request):
    return render(request, 'pages/post.html')

def signin_view(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect("/")
        return render(request, 'pages/signin.html', {'form':form})
    form = SigninForm()
    return render(request, 'pages/signin.html', {'form':form})

def signup_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
        return render(request, 'pages/signup.html', {'form':form})
            
    form = RegistrationForm()
    return render(request, 'pages/signup.html', {'form':form})

def profile(request):
    return render(request, 'pages/profile.html')