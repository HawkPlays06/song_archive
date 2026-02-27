from django.db import models

# Create your models here.
class Account(models.Model):
    account_ID = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=255, null=False)
    e_mail = models.EmailField(max_length=255, null=False, unique=True, error_messages={"unique": "Email already registered. Log in instead."})
    DOB = models.DateField(null=False)
    date_of_creation = models.DateField(auto_now_add=True, null=False)
    account_image = models.ImageField(upload_to="accounts/")

    def delete(self, *args, **kwargs):
        if self.account_image:
            self.account_image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        try:
            account_image = self.account_image.file
        except ValueError:
            account_image = "None"
        return f"{self.account_ID} | {self.account_name} | {self.e_mail} | {self.DOB} | {self.date_of_creation} | {account_image}"
    
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

class Publisher(models.Model):
    publisher_ID = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=255, null=False)

    def __str__(self):
            return f""

class Playlist(models.Model):
    playlist_ID = models.AutoField(primary_key=True)
    playlist_name = models.CharField(max_length=255, null=False)
    owner_account_ID = models.ForeignKey(Account, on_delete=models.CASCADE, null=False)
    playlist_image = models.ImageField(upload_to="playlist/")

    def delete(self, *args, **kwargs):
        if self.playlist_image:
            self.playlist_image.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f""

class Album(models.Model):
    album_ID = models.AutoField(primary_key=True)
    artist_ID = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    publisher_ID = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=False)
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

class PlaylistTrack(models.Model):
    playlist_ID = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=False)
    spotify_URL = models.ForeignKey(Track, on_delete=models.CASCADE, null=False)
    position = models.PositiveIntegerField(null=False)
    added_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["playlist_ID", "spotify_URL"], name="playlist_track_PK")
        ]

    def __str__(self):
        return f""