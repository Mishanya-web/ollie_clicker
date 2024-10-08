from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Gamer

def index(request):
    return redirect('login_view')
def register_view(request):
    if request.user.is_authenticated:
        return redirect('clicker_view')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                Gamer.objects.create(user=user)
                login(request, user)
                return redirect('clicker_view')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('clicker_view')
    else:
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('clicker_view')
        else:
            form = UserLoginForm()
        return render(request, 'login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login_view')

def clicker_view(request):
    if request.user.is_authenticated:
        return render(request, 'clicker.html')
    else: return redirect('login_view')

def leaderboard(request):
    if request.user.is_authenticated:
        gamers = Gamer.objects.order_by('-score')
        return render(request, 'leaderboard.html', {'gamers': gamers})
    else: return redirect('login_view')
