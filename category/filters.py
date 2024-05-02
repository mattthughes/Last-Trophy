import django_filters
from trophy_hunter.models import Game


class GameFilter(django_filters.FilterSet):
    hours = django_filters.RangeFilter()

    class Meta:
        model = Game
        fields = {
            'title': ['icontains'],
            'genre': ['exact'],

        }
