from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms

# Create your views here.
def home_view(request):
    return render(request, "song_archive/home.html")

def sign_up_view(request):
    if request.method == "POST":
        form = forms.Signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.Signup_form()
    
    context = {"form" : form}
    return render(request, "song_archive/sign up.html", context)

def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = forms.LoginForm(request=request)

    return render(request, "song_archive/log in.html", {"form": form})