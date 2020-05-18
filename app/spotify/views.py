from django.shortcuts import render
from django.http import HttpResponse
from .models import Search, Playlist_search, Track_search


def index(request):
    context = {
        "searches": Search.objects.all(),
    }
    return render(request, "spotify/landing.html", context)


def search(request, search_id):
    context = {
        "search": Search.objects.get(pk=search_id),
        "playlists": Playlist_search.objects.filter(environment=search_id),
        "tracks": Track_search.objects.filter(environment=search_id),
    }
    return render(request, "spotify/search.html", context)


def playlist(request, search_id, playlist_id):
    context = {
        "playlist": Playlist_search.objects.get(pk=playlist_id),
    }
    return render(request, "spotify/playlist.html", context)


def track(request, search_id, track_id):
    context = {
        "track": Track_search.objects.get(pk=track_id),
    }
    return render(request, "spotify/track.html", context)
