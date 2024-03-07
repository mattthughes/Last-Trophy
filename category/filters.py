import django_filters
from trophy_hunter.models import Games

class GameFilter(django_filters.FilterSet):
    model = Games
    fields = ['title', 'genre']