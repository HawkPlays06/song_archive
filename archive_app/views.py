from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . import forms

def home_view(request):
    return render(request, "song_archive/home.html")

def sign_up_view(request):
    if request.method == "POST":
        form = forms.Signup_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = forms.Signup_form()
    
    return render(request, "song_archive/sign up.html", {"form" : form})

def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = forms.LoginForm(request=request)

    return render(request, "song_archive/log in.html", {"form": form})

@login_required
def account_view(request):
    return render(request, "song_archive/account/index.html")

@login_required
def change_email_view(request):
    if request.method == "POST":
        form = forms.EmailChange(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data["email"]
            request.user.save()
            return redirect("account")
    else:
        form = forms.EmailChange(initial={"email": request.user.email})

    return render(request, "song_archive/account/change email.html", {"form": form})

@login_required
def change_password_view(request):
    if request.method == "POST":
        form = forms.PasswordChange(request.POST)
        if form.is_valid():
            return redirect("account")
    else:
        form = forms.PasswordChange()

    return render(request, "song_archive/account/change password.html", {"form": form})