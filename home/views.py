from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, SigninForm, InfoForm, PostForm
from .models import InfomationEnterprise, Post
from .facebookapi import facebook
# Create your views here.
def home_view(request):
    if request.user.username:
        return HttpResponseRedirect('post/')
    return render(request, 'pages/recruitment.html')


def signin_view(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect("/")
        return render(request, 'pages/login.html', {'form':form})
    form = SigninForm()
    return render(request, 'pages/login.html', {'form':form})

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
        else:
            return render(request, 'pages/register.html', {'form':form})
            
    form = RegistrationForm()
    return render(request, 'pages/register.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def profile(request):
    return render(request, 'pages/profile.html')

def infoform(request):
    if request.method == "POST":
        form = InfoForm(request.POST)
        if form.is_valid():
            form = InfoForm(request.POST)
            form.save()
        else:
            print(form.errors)
            return render(request, 'pages/infomation_enterprise.html', {'form':form}) 
    if request.user.username:
        all_info = InfomationEnterprise.objects.all()  
        for i in all_info:
            if i.username == request.user.username:
                return HttpResponseRedirect('/post')
        form = InfoForm()
        return render(request, 'pages/infomation_enterprise.html',{'form':form})
    else:
        return HttpResponseRedirect('/signin')

def post_view(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            info = InfomationEnterprise.objects.get(username = request.user.username)
            company = info.company
            local = info.local
            title = form.cleaned_data['title']
            speciality = form.cleaned_data['speciality']
            workplace = form.cleaned_data['workplace']
            amount = form.cleaned_data['amount']
            rank = form.cleaned_data['rank']
            worktime = form.cleaned_data['worktime']
            sex = form.cleaned_data['sex']
            exp = form.cleaned_data['exp']
            salary = form.cleaned_data['salary']
            deadline = form.cleaned_data['deadline']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            des_of_company = form.cleaned_data['des_of_company']
            describe = form.cleaned_data['describe']
            require = form.cleaned_data['require']
            benefit = form.cleaned_data['benefit']
            skill = form.cleaned_data['skill']
            info.post_set.create(title = title,speciality=speciality,workplace=workplace,amount=amount,rank=rank,worktime=worktime,sex=sex,exp=exp,salary=salary,deadline=deadline,name=name,email=email,contact=contact,des_of_company=des_of_company,describe=describe,require=require,benefit=benefit,skill=skill)
        else:
            print(form.errors)
            return render(request, 'pages/post.html', {'form':form})
    if request.user.username:
        all_info = InfomationEnterprise.objects.all()
        for i in all_info:
            if i.username == request.user.username:
                form = PostForm()
                return render(request, 'pages/post.html', {'form':form})
        return HttpResponseRedirect("/infoform")         
    else:
        return HttpResponseRedirect('/signin')


def listpost(request):
    info = InfomationEnterprise.objects.get(username = request.user.username)
    post = info.post_set.all()
    return render(request, 'pages/listpost.html', {'post':post})


def newfeed(request):
    info = InfomationEnterprise.objects.all()
    post = Post.objects.all().order_by('-time')
    return render(request, 'pages/newfeed.html', {'info':info, 'post':post})