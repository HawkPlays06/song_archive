from django import forms
from . import models

class AccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = ["account_name", "e_mail", "DOB", "account_image"]
        widgets = {
            
        }

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

