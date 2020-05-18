from django.db import models


class Search(models.Model):
    name = models.CharField(max_length=200)
    genres = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Search environment"
        verbose_name_plural = "Search environments"


class Playlist_search(models.Model):
    name = models.CharField(max_length=200)
    environment = models.ForeignKey(Search, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Playlist search"
        verbose_name_plural = "Playlist searches"


class Track_search(models.Model):
    name = models.CharField(max_length=200)
    environment = models.ForeignKey(Search, on_delete=models.CASCADE)
    dancability = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Track search"
        verbose_name_plural = "Track searches"
