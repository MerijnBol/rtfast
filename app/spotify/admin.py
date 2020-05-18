from django.contrib import admin

from .models import Search, Playlist_search, Track_search

admin.site.register(Search)
admin.site.register(Playlist_search)
admin.site.register(Track_search)
