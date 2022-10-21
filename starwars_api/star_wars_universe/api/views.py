from django.shortcuts import get_object_or_404
from rest_framework import filters

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from star_wars_universe.api.serializers import CharacterSerializer, PlanetSerializer, MovieSerializer
from star_wars_universe.models import Character, Planet, Movie


class CharacterViewSet(viewsets.ModelViewSet):
    queryset= Character.objects.all()
    serializer_class= CharacterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self,request):
        queryset= Character.objects.all()
        serializer = CharacterSerializer(queryset, many=True)
        return Response(serializer.data)
    
           
    def retrieve(self, request, pk=None, *args, **kwargs):
        character = self.get_queryset(pk)
        if character:
            character_serializer= CharacterSerializer(character)
            return Response(character_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'There is no character with this data'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            character_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if character_serializer.is_valid():
                character_serializer.save()
                return Response(character_serializer.data)
            return Response(character_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self, request, pk=None):
        character = self.get_queryset(pk)
        if character:
            character_serializer= CharacterSerializer(character)
            character.delete()
            return Response({'message':'Character eliminated successfully!'}, status=status.HTTP_200_OK)
        return Response({'error':'There is no character with this data'}, status=status.HTTP_400_BAD_REQUEST)

class PlanetViewSet(viewsets.ModelViewSet):
    queryset= Planet.objects.all()
    serializer_class= PlanetSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self,request):
        queryset= Planet.objects.all()
        serializer = PlanetSerializer(queryset, many=True)
        return Response(serializer.data)
           
    def retrieve(self, request, pk=None, *args, **kwargs):
        planet = self.get_queryset(pk)
        if planet:
            planet_serializer= PlanetSerializer(planet)
            return Response(planet_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'There is no planet with this data'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            planet_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if planet_serializer.is_valid():
                planet_serializer.save()
                return Response(planet_serializer.data)
            return Response(planet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieViewSet(viewsets.ModelViewSet):
    queryset= Movie.objects.all()
    serializer_class= MovieSerializer

    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self,request):
        queryset= Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)
    
           
    def retrieve(self, request, pk=None, *args, **kwargs):
        movie = self.get_queryset(pk)
        if movie:
            movie_serializer= MovieSerializer(movie)
            return Response(movie_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'There is no movie with this data'}, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        if self.get_queryset(pk):
            movie_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if movie_serializer.is_valid():
                movie_serializer.save()
                return Response(movie_serializer.data)
            return Response(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def destroy(self, request, pk=None):
        movie = self.get_queryset(pk)
        if movie:
            movie_serializer= MovieSerializer(movie)
            movie.delete()
            return Response({'message':'Movie eliminated successfully!'}, status=status.HTTP_200_OK)
        return Response({'error':'There is no movie with this data'}, status=status.HTTP_400_BAD_REQUEST)
    
