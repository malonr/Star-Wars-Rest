from rest_framework import serializers
from star_wars_universe.models import (
    Planet,
    Character,
    Movie,
)

class CharacterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Character
        fields = ['name', 'gender','movies']
        
class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name']
    
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 
                  'episode_number',
                  'opening_text', 
                  'director', 'producer',
                  'release_date', 
                  'characters' , 'planets'
                  ]
