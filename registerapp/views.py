from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#Develop by Haseeb Asghar
#https://www.linkedin.com/in/infohaseeb/
#https://github.com/infohaseeb

def LoginUser(request):
    if request.user.username=="":
        return render(request,"login.html")
    else:
        return HttpResponseRedirect("/homepage")

@login_required(login_url="/loginuser/")
def HomePage(request):
    return render(request, "home.html")

def clicklogin(request):
    if request.method!="POST":
        return HttpResponse("<h1> Methoid not allowed<h1>")
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        
        user=authenticate(username=username,password=password)
        if user!=None:
            login(request,user)
            return HttpResponseRedirect('/homepage')
        else:
            messages.error(request, "Invalid Login")
            return HttpResponseRedirect('/loginuser')

def LogoutUser(request):
    logout(request)
    request.user=None
    return HttpResponseRedirect("/loginuser")       




def RegisterUser(request):
    if request.user==None or request.user =="" or request.user.username=="":
        return render(request,"register.html")
    else:
        return HttpResponseRedirect("/homepage")        


def ClickRegister(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            messages.success(request, "User Created Successfully")
            return HttpResponseRedirect('/register_user')
        else:
            messages.error(request, "Email or Username Already Exist")
            return HttpResponseRedirect('/register_user')