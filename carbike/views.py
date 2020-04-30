from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vehicle
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):

    vehs = Vehicle.objects.all()
    return render(request,'index.html',{'vehs':vehs})

def news(request):
    return render(request,'news.html',)

def contact(request):
    return render(request,'contact.html',)

def accessories(request):
    return render(request,'accessories.html',)

def bikes(request):
    return render(request,'bikes.html',)

def cars(request):
    return render(request,'cars.html',)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password =password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html' )
def logout(request):
    auth.logout(request)
    return redirect('/')


def form(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('form')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('form')
            else:
                user = User.objects.create_user(username=username, password = password1, email = email, first_name = first_name,last_name =last_name)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password incorrect')
            return redirect('form')

        return redirect('/')
    else:
        return render(request,'form.html',)

