from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from . import forms

# Create your views here.
def home_view(request):
    return render(request, "song_archive/home.html")

def sign_up_view(request):
    if request.method == "POST":
        form = forms.AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.AccountForm()
    
    context = {"form" : form}
    return render(request, "song_archive/sign up.html", context)

def log_in_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AuthenticationForm()
    
    context = {"form" : form}
    return render(request, "song_archive/log in.html", context)
