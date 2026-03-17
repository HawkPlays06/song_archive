from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from . import models

def home_view(request):
    return render(request, "song_archive/home.html")

# region account views

def account_sign_up_view(request):
    if request.method == "POST":
        form = forms.Account_signup_form(request.POST)
        if form.is_valid():

            account_name = form.cleaned_data["account_name"]
            email = form.cleaned_data["email"]
            dob = form.cleaned_data["DOB"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username = account_name,
                password = password,
                email = email
            )

            models.Profile.objects.create(
                user = user,
                account_name = account_name,
                DOB = dob
            )

            login(request, user)
            return redirect("home")
    else:
        form = forms.Account_signup_form()
    
    return render(request, "song_archive/account/sign up.html", {"form" : form})

def account_login_view(request):
    if request.method == "POST":
        form = forms.Account_login_form(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = forms.Account_login_form(request=request)

    return render(request, "song_archive/account/log in.html", {"form": form})

@login_required
def account_view(request):
    return render(request, "song_archive/account/index.html")

@login_required
def change_email_view(request):
    if request.method == "POST":
        form = forms.Email_change_form(request.POST)
        if form.is_valid():
            request.user.email = form.cleaned_data["email"]
            request.user.save()
            return redirect("account")
    else:
        form = forms.Email_change_form(initial={"email": request.user.email})

    return render(request, "song_archive/account/change email.html", {"form": form})

@login_required
def change_password_view(request):
    if request.method == "POST":
        form = forms.Password_change_form(request.POST)
        if form.is_valid():
            return redirect("account")
    else:
        form = forms.Password_change_form()

    return render(request, "song_archive/account/change password.html", {"form": form})

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("home")
    
    return render(request, "song_archive/account/delete account.html")

# endregion

def artist_sign_up_view(request):
    if request.method == "POST":
        form = forms.Artist_signup_form(request.POST)
        if form.is_valid():

            artist_name = form.cleaned_data["artist_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = User.objects.create_user(
                username = artist_name,
                password = password,
                email = email
            )

            models.Artist.objects.create(
                user = user,
                artist_name = artist_name
            )
        
            login(request, user)
            return redirect("home")
        
    else:
        form = forms.Artist_signup_form()
    return render(request, "song_archive/artist/sign up.html", {"form" : form})