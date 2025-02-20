from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def login(request):
    #retrieves data
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #authenticates user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'account/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm-password')

        if not username or not email or not password or not confirmPassword:
            messages.error(request, "All fields are required!")
            return redirect('signup')

        if password != confirmPassword:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, f"Welcome, {username}!")
        return redirect('/')

    return render(request, 'account/signup.html')

def home(request):
    return render(request, 'main/home.html')