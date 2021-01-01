from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.contrib.auth.hashers import make_password,check_password

from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from .forms import LoginForm,SignupForm
from django.contrib.auth.models import User





# Create your views here.
def user_login(request):
    
    if request.method=='POST':
        form=LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            obj=authenticate(username=uname,password=upass)
            if obj is not None:
                login(request,obj)
                messages.success(request,'Successfully Login ! ')
                return redirect('home')
                    
    else:
        form=LoginForm()
    return render(request,'core/login.html',{'form':form,'homee':'active'})


def logout_form(request):
    
    logout(request)
    messages.success(request,'Logout ! ')
    return redirect('login')

def signup_form(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignupForm(request.POST)
            
            if form.is_valid():
                messages.success(request,'Congratulation ,Successfully Signup ')
                user=form.save()
                
                
                return redirect('login')
        else:
            form=SignupForm()
        return render(request,'core/signup.html',{'form':form,'homee':'active'})
    else:

        return redirect('home')
    



def home(request):
    context={'home':'active'}
    return render(request,'core/home.html',context)

def contact(request):
   
    context={'contact':'active'}
    return render(request,'core/contact.html',context)

def projects(request):
   
    context={'projects':'active'}
    return render(request,'core/projects.html',context)