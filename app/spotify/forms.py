from django import forms


class searchForm(forms.Form):
    querry = forms.CharField(max_length=100, required=True)
    # Must equal Spotify types: album, artist, playlist, track, show, episode.
    track = forms.BooleanField(label="Songs", required=False)
    album = forms.BooleanField(label="Albums", required=False)
    artist = forms.BooleanField(label="Artists", required=False)
    playlist = forms.BooleanField(label="Playlists", required=False)
