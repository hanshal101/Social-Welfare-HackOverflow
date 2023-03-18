from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Locate, News
from .models import Updates



def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {'news' :news})

def chat(request):
    return render(request, 'chat.html', {'chat' :chat})

def updates(request):
    updates = Updates.objects.all()
    return render(request, 'updates.html', {'updates' : updates})


def locate(request):
    locate = Locate.objects.all()
    return render(request, 'locate.html', {'locate' : locate})

def createaccount(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Already Exists')

            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username Already Exists')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)

            
        else:
            messages.info(request, 'Passwod not same')
            return redirect('createacccount')

            user.save()

    return render(request, 'createaccount.html')

def login(request):
    if request.method == 'POST':

       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username = username, password = password)

       if user is not None:
           auth.login(request, user)
           return redirect('/')
       else:
           messages.info(request, 'Credentials Invalid')
           return redirect('login')
       
    else:
        return render(request, 'login.html')
    
    


