from django.urls import path


from . import views

app_name = "spotify"
urlpatterns = [
    # spotify/
    path("", views.index, name="index"),
    # spotify/5
    path("<int:search_id>/", views.search, name="search"),
    # spotify/5/playlist
    path("<int:search_id>/playlist_<playlist_id>/", views.playlist, name="playlist"),
    # spotify/5/track
    path("<int:search_id>/track_<track_id>/", views.track, name="track"),
]
