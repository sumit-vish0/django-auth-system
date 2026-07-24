from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def register_view(request):
    context={
        'errors' :[]
    }
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        confirm_password = request.POST.get('pwd2')
        
        if User.objects.filter(username=username).exists():
            context['errors'].append('Username already exists')
            
        if password != confirm_password:
                context['errors'].append('Password do not match')
                
        temp_user=User(username=username,email=email)

        try:
            validate_password(password=password, user=temp_user)
        except ValidationError as error:
            context['errors'].extend(error.messages)
        
        if not context['errors']:
            user=User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
        
    return render(request,'register.html',context)



def signin_view(request):
    
    context={}
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            
            login(request,user)
            return redirect('home')
        else:
            context["error"] = "Invalid Credentials"

    return render(request, "signin.html", context)

def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def signout_view(request):
    logout(request)
    return redirect('login')