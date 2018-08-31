from django.urls import path
from . import views

urlpatterns = [
    path('',        views.home, name = 'home'),
    path('Album/',  views.Album, name = 'Album')
    #path('song/',   views.song, name = 'song')
]