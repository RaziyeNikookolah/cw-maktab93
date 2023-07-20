from django.shortcuts import render
from .models import Artist, Album, Song

def display_artists(request):
    artists= Artist.objects.all()
    return render(request , 'artists_list.html' , {'artists':artists})

def display_artists_by_genre(request , genre):
    artists= Artist.objects.filter(genre= genre)
    return render(request , 'artists_list_by_genre.html' , {'artists':artists , 'genre' : genre})
 
