from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')

def signin_view(request):
    return render(request, 'pages/signin.html')

def signup_view(request):
    return render(request, 'pages/signup.html')