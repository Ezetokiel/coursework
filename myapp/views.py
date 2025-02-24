from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def loginPage(request):
    #retrieves data
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticates user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'account/login.html')

def homePage(request):
    return render(request, 'main/home.html')

def schedulePage(request):
    
    return render(request, 'main/schedule.html')

def signupPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm-password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Please choose a different one.")
            return redirect('signup')

        # Check if the email already exists (optional)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use! Try another one.")
            return redirect('signup')

        # Check if passwords match
        if password != confirmPassword:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        user = User.objects.create_user(username, email, password)
        authenticatedUser = authenticate(request, username=username, password=password)
        login(request, authenticatedUser)
        messages.success(request, f"Welcome, {username}!")
        return redirect('home')
    return render(request, 'account/signup.html')
