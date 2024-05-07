import django_filters
from trophy_hunter.models import Game


class GameFilter(django_filters.FilterSet):

    class Meta:
        model = Game
        fields = {
            'title': ['icontains'],
            'genre': ['exact'],
            'hours': ['lt', 'gt']
        }
