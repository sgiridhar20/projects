from django.shortcuts import render,redirect
from django.contrib.auth.models import  User as Us,auth
from django.contrib import messages



# Create your views here
#def login(request):
    #return render(request,"login.html")  

def register(request):
    if request=="POST":
      
        first_name=request.POST['first_name']
        second_name=request.POST['second_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1 == password2:
            if Us.objects.filter(username=username).exists:
                   messages.info(request,'Already exists...')
                   return redirect('register')
            elif Us.objects.filter(email=email).exists():
                   messages.info(request,'Email Tken...')
                   return redirect('register')

            else:
                   User=Us.objects.create_User(username='username',password='password1',email='email',first_name=first_name,second_name='second_name')
                   User.save()
                   print('user created')

        else:
            messages.info(request,"password not matching")
            return redirect('register')   

    
    else:
        return render(request, "register.html")

def login(request):
    if request.method=="Post":
        username=request.Post['username']
        password=request.Post['password']
        user.auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            message.info(request,'sorry invalid credentials')   
            return redirect('login') 
    else:
        return redirect(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")




##bye 31.12.2020           




      
