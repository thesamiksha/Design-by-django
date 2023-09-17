from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from tells.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def home(request):
    #return HttpResponse("This is home page")
    return render (request,'home.html')
def dailyneeds(request):
    return HttpResponse("This is dailyneeds page")
def electronics(request):
    return HttpResponse("This is electronics & Appliances page")
def lifestyle (request):
    return HttpResponse("This is lifestyle page")
def mens(request):
    return HttpResponse("This is mens page")
def kiddo(request):
    return HttpResponse("This is kiddo page")
def womens(request):
    return HttpResponse("This is womens page")
def books (request):
    return HttpResponse("This is books  page")
def globals(request):
    return HttpResponse("This is shop globals page")
def RICE (request):
    return render(request,'RICE.html') 
def contact(request):
    #return HttpResponse ("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.info(request, 'your message has been sent!!.')

    return render(request,'contact.html')
def ourstore(request):
    return render (request,'ourstore.html')
def careers(request):
    return render (request,'careers.html')
def FAQ(request): 
    return render(request,'FAQ.html')
def signin(request):
    if request.method =="POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        User = authenticate(username=username,password=pass1)
        if User is not None:
            login(request,User)
            fname = User.first_name
            return render(request,"profile.html",{'fname':fname})
        else:
            messages.error(request,"Bad credential")
            return redirect("signin")
         
    return render(request,"signin.html")
def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        fname = request.POST.get("fname")
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if User.objects.filter(username=username):
            messages.error(request,"This username is already exist !! ")
            return redirect('signup')
        if User.objects.filter(email=email):
             messages.error(request,'Sorry,This email is already exist !!')
             return redirect('signup')
        if pass1 != pass2:
            messages.error(request,'Password is incorrect!!')

            return redirect('signup')
        if len(username)>15:
            messages.error(request,"username must be under 15 characters")
        
            return redirect("signup")


            
       

        
        myuser = User.objects.create(username=username,email=email,password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        messages.success(request,"Your account has been sucessfully signup")
        return redirect("/signin")
    return render (request, 'signup.html')


def profile(request):
    return render (request,'profile.html')