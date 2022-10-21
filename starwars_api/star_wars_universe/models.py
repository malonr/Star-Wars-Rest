from django.db import models
from utils.models.base import StarWarsModel


class Planet(StarWarsModel):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Character(StarWarsModel):

    name = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=40, blank=True)
    planet_id = models.ForeignKey(Planet, related_name="residents", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Movie(StarWarsModel):
    
    title = models.CharField(max_length=100)
    episode_number = models.IntegerField()
    opening_text = models.TextField(max_length=1000)
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    release_date = models.DateField()
    characters = models.ManyToManyField(
        Character,
        related_name="movies",
        blank=True
    )
    planets = models.ManyToManyField(
        Planet,
        related_name="movies",
        blank=True
    )

    def __str__(self):
        return self.title