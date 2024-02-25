from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request,'homepage.html')


def signup(request):
    
    if request.method == 'POST':
        
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
                
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request,'Username already exist! try other username.')
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request,'Email already registered!')
            return redirect('home')
        if len(username)>10:
            messages.error(request,'Username must be under 10 characters!')
            return redirect('home')
        if pass1 != pass2:
            messages.error('Passwords does not match!')
            return redirect('home')
        if not username.isalnum():
            messages.error('Username must be Alpha-Numeric!')
            return redirect('home')
        
        
        new_user = User.objects.create_user(username,email,pass1)
        new_user.first_name = fname
        new_user.last_name = lname
        
        new_user.save()
        
        messages.success(request,'Sign up successful')
        
        return redirect('signin')
    
    return render(request,'authentication/signup.html')

def signin(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username,password=pass1)
        
        if user is not None:
            login(request,user )
            fname = user.first_name
            return render(request,'authentication/index.html',{'fname': fname})
        else:
            messages.error(request,'Bad credentials')
            return redirect('home')
    
    return render(request,'homepage.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('home')