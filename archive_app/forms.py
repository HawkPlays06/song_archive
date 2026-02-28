from django import forms
from datetime import date
from dateutil.relativedelta import relativedelta
from . import models

class AccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ["account_name", "e_mail", "DOB", "password_hash"]
        widgets = {
            "account_name" : forms.TextInput(attrs={"placeholder": "Username"}),
            "e_mail" : forms.EmailInput(attrs={"placeholder": "E-mail address"}),
            "DOB": forms.DateInput(attrs={"type": "date"}),
            "password_hash" : forms.PasswordInput(attrs={"placeholder" : "Password"})
        }
    
    def clean_DOB(self):
        dob = self.cleaned_data.get("DOB")
        if dob:
            if dob > date.today():
                raise forms.ValidationError("That date is in the future.")
            elif dob > date.today() - relativedelta(years=13):
                raise forms.ValidationError("You must be at least 13 years old.")
        
        return dob
    
    def clean_password_hash(self):
        password = self.cleaned_data.get("password_hash")
        return models.hash_password(password)
"""
class ArtistForm(forms.ModelForm):
    class Meta:
        model = models.Artist
        fields = [""]
        widgets = {

        }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = [""]
        widgets = {

        }

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = models.Playlist
        fields = [""]
        widgets = {

        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = [""]
        widgets = {

        }

class TrackForm(forms.ModelForm):
    class Meta:
        model = models.Track
        fields = [""]
        widgets = {

        }

"""