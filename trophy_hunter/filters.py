import django_filters
from trophy_hunter.models import Game

class GameFilter(django_filters.FilterSet):
    model = Game
    fields = ['title', 'genre', 'trophy_count', 'hours']