from django.contrib import admin
from . import models

admin.site.register(models.Account)
admin.site.register(models.Artist)
admin.site.register(models.Publisher)
admin.site.register(models.Playlist)
admin.site.register(models.Album)
admin.site.register(models.Track)
admin.site.register(models.TrackArtist)
admin.site.register(models.PlaylistTrack)