from django import forms
from django.contrib.auth.models import User
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.utils.html import format_html
from django.urls import reverse
from . import models

class Account_signup_form(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "E-mail address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password"}), label="Password")

    account_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder": "Username"}))
    DOB = forms.DateField(widget=forms.DateInput(attrs={"type" : "date"}))

    class Meta:
        model = User
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email=email).exists():
            login_url = reverse("log in")
            raise ValidationError(
            format_html(
                'Email already registered. <a href="{}">Log in </a> instead.',
                login_url
            )
        )
        return email
    
    def clean_DOB(self):
        dob = self.cleaned_data["DOB"]
        if dob:
            if dob > date.today():
                raise forms.ValidationError("That date is in the future.")
            elif dob > date.today() - relativedelta(years=13):
                raise forms.ValidationError("You must be at least 13 years old.")
        
        return dob
    
class Account_login_form(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

class Email_change_form(forms.Form):
    email = forms.EmailField(label="New email")

class Password_change_form(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "New password"})
    )

class Artist_signup_form(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "E-mail address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password"}), label="Password")

    artist_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder": "Artist Name"}))

    class Meta:
        model = User
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email=email).exists():
            login_url = reverse("log in")
            raise ValidationError(
            format_html(
                'Email already registered. <a href="{}">Log in </a> instead.',
                login_url
            )
        )
        return email