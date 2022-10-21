from django.urls import path, include
from rest_framework.routers import DefaultRouter
from star_wars_universe.api.views import CharacterViewSet, MovieViewSet, PlanetViewSet

router = DefaultRouter()

router.register(r'characters',CharacterViewSet,basename = 'characters')
router.register(r'movies',MovieViewSet,basename = 'movies')
router.register(r'planets',PlanetViewSet,basename = 'planets')


urlpatterns = router.urls