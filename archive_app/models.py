from django.db import models
from django.contrib.auth.models import User

# structure of Profile:

# user CASCADE linked to User PK
# account_name string(255) not null
# DOB DD-MM-YYYY not null
# profile_image image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    account_name = models.CharField(max_length=255, null=False)
    DOB = models.DateField(null=False)
    profile_image = models.ImageField(upload_to="Profiles/")

    # deletes image
    def delete(self, *args, **kwargs):
        user = self.user
        if self.profile_image:
            self.profile_image.delete(save=False)
        super().delete(*args, **kwargs)
        user.delete()

    # if image file doesn't exist, add None
    def __str__(self):
        try:
            profile_image = self.profile_image.file
        except ValueError:
            profile_image = "None"
        return f"{self.user} | {self.account_name} | {self.DOB} | {profile_image}"

# structure of Artist:

# user CASCADE linked to User PK
# artist_name string(255) not null
# artist_image image
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    artist_name = models.CharField(max_length=255, null=False)
    artist_image = models.ImageField(upload_to="artist/")

    # deletes image
    def delete(self, *args, **kwargs):
        if self.artist_image:
            self.artist_image.delete(save=False)
        super().delete(*args, **kwargs)

    # if image file doesn't exist, add none
    def __str__(self):
        try:
            artist_image = self.artist_image.file
        except ValueError:
            artist_image = "None"
        return f"{self.user} | {self.artist_name} | {artist_image}"


# structure of Album:

# album_ID auto field PK
# artist_ID FK to Artist's PK (User)  not null
# title string(255) not null
# release_date DD-MM-YYYY not null
# album_image image

class Album(models.Model):
    album_ID = models.AutoField(primary_key=True)
    artist_ID = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=255, null=False)
    release_date = models.DateField(null=False)
    album_image = models.ImageField(upload_to="album/", null=False)
    
    # delete image
    def delete(self, *args, **kwargs):
        if self.album_image:
            self.album_image.delete(save=False)
        super().delete(*args, **kwargs)

    # need to set up
    def __str__(self):
        return f""

# structure of Track:

# spotify_URL string(255) not null
# track_name string(255) not null
# album_ID FK to album's PK (album_ID) not null CASCADE
# track_number positive number not null
# explicit boolean not null
# duration positive number not null
# tempo positive number not null
# time_signature positive number not null 

class Track(models.Model):
    spotify_URL = models.CharField(max_length=255, null=False, primary_key=True)
    track_name = models.CharField(max_length=255, null=False)
    album_ID = models.ForeignKey(Album,on_delete=models.CASCADE, null=False)
    track_number = models.PositiveIntegerField(null=False)
    explicit = models.BooleanField(null=False)
    duration = models.PositiveIntegerField(null=False)
    tempo = models.PositiveIntegerField(null=False)
    time_signature = models.PositiveIntegerField(null=False)

    # need to set up
    def __str__(self):
        return f""

# structure of TrackArtist:

# spotify_URL FK to Track's PK (spotify_URL) not null CASCADE
# artist_ID FK to Artist's PK (user) not null CASCADE
# role string(7) choices are PRIMARY and OTHER

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

    # need to set up
    def __str__(self):
        return f""