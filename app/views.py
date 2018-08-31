from django.shortcuts import render
from app.models import Album,Song

# Create your views here.
def home(request):

	return render(request,'home.html')


def Album(request):
	song  = Song.objects.all()
	#album = Album.objects.all()
	return render (request,'Album.html', {'Song':song})
"""
,'Album':album
def (request):
	song  = Song.Objects.all()
	album = Album.objects.all()
	return render (request,'Album.html', {'Song':song,'Album':album})
"""
	