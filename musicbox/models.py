from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(max_length=150)


class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    duration = models.IntegerField()
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='songs')