from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Artist)
admin.site.register(models.Publisher)
admin.site.register(models.Album)
admin.site.register(models.Track)
admin.site.register(models.TrackArtist)