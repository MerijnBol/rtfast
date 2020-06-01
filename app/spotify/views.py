import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from urllib.parse import quote

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# from .models import Search, Playlist_search, Track_search
from .forms import searchForm

from .views_utils import collect_checkboxes, add_results_to_context

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


def index(request):
    context = {}
    context["form"] = searchForm()
    return render(request, "spotify/index.html", context)


def results(request):
    context = {}
    # Retreive the form data, or redirect to search page
    if request.method == "POST":
        form = searchForm(request.POST)
        if not form.is_valid():
            return
    else:
        form = searchForm()
        return HttpResponseRedirect("/spotify")
    context["form"] = form

    # get the search results
    data = request.POST
    search_q = quote(data["querry"])
    search_types = collect_checkboxes(data)
    # No inputs defaults to search for songs
    if len(search_types) == 0:
        search_types = ["track"]
    results = spotify.search(q=search_q, type=search_types)
    add_results_to_context(context, results)

    return render(request, "spotify/results.html", context)


# views for model tree test, not active now.

# def index(request):
#     context = {
#         "searches": Search.objects.all(),
#     }
#     return render(request, "spotify/landing.html", context)


# def search(request, search_id):
#     context = {
#         "search": Search.objects.get(pk=search_id),
#         "playlists": Playlist_search.objects.filter(environment=search_id),
#         "tracks": Track_search.objects.filter(environment=search_id),
#     }
#     return render(request, "spotify/search.html", context)


# def playlist(request, search_id, playlist_id):
#     context = {
#         "playlist": Playlist_search.objects.get(pk=playlist_id),
#     }
#     return render(request, "spotify/playlist.html", context)


# def track(request, search_id, track_id):
#     context = {
#         "track": Track_search.objects.get(pk=track_id),
#     }
#     return render(request, "spotify/track.html", context)
