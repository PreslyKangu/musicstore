from django.db import models

# Create your models here.

class Album(models.Model):
	"""docstring for Halflondon"""
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=1025)
	album_logo = models.CharField(max_length=1000)

	def __unicode__(self):
		return self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete =models.CASCADE)
	file_type = models.CharField(max_length=150)
	song_type =models.CharField(max_length=500)


	def __unicode__(self):
		return self.album