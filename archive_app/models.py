from django.db import models
from django.contrib.auth.models import User
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    account_name = models.CharField(max_length=255, null=False)
    DOB = models.DateField(null=False)
    profile_image = models.ImageField(upload_to="Profiles/")

    def delete(self, *args, **kwargs):
        if self.profile_image:
            self.profile_image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        try:
            profile_image = self.profile_image.file
        except ValueError:
            profile_image = "None"
        return f"{self.user} | {self.account_name} | {self.DOB} | {profile_image}"

class Artist(models.Model):
    artist_ID = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255, null=False)
    artist_image = models.ImageField(upload_to="artist/")

    def delete(self, *args, **kwargs):
        if self.artist_image:
            self.artist_image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f""

class Album(models.Model):
    album_ID = models.AutoField(primary_key=True)
    artist_ID = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False)
    release_date = models.DateField(null=False)
    album_image = models.ImageField(upload_to="album/", null=False)
    
    def delete(self, *args, **kwargs):
        if self.album_image:
            self.album_image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f""

class Track(models.Model):
    spotify_URL = models.CharField(max_length=255, null=False, primary_key=True)
    track_name = models.CharField(max_length=255, null=False)
    album_ID = models.ForeignKey(Album,on_delete=models.CASCADE, null=False)
    track_number = models.PositiveIntegerField(null=False)
    explicit = models.BooleanField(null=False)
    duration = models.PositiveIntegerField(null=False)
    tempo = models.PositiveIntegerField(null=False)
    time_signature = models.PositiveIntegerField(null=False)

    def __str__(self):
        return f""

class TrackArtist(models.Model):

    class Role(models.TextChoices):
        PRIMARY = "PRIMARY", "Primary artist"
        OTHER = "OTHER", "Other artist"

    spotify_URL = models.ForeignKey(Track,on_delete=models.CASCADE, null=False)
    artist_ID = models.ForeignKey(Artist,on_delete=models.CASCADE, null=False)
    role = models.CharField(max_length=7, choices=Role.choices)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["spotify_URL", "artist_ID"], name="track_artist_PK")
        ]

    def __str__(self):
        return f""