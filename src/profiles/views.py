from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PersonInfoCreationForm, LoginForm
from src.pages import views
# Create your views here.


def sign_in_view(request):
    form = PersonInfoCreationForm(request.POST)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "signOrLogin.html", context)


def login_view(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "login.html", context)


def authentication_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return views.home_view(request)
    else:
        messages.error(request, 'You have to sign in first')
    return sign_in_view(request)


def logout_view(request):
    logout(request)
    return render(request, "home.html", {})