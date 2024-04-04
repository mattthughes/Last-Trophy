from django import forms
from trophy_hunter.models import Game


class GameForm(forms.ModelForm):
    """
    Form class for users to create a guide
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Game
        fields = (
            'title',
            'slug',
            'author',
            'featured_image',
            'genre',
            'trophy_count',
            'hours',
            'game_score',
            'rating')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'trophy_count': forms.TextInput(attrs={'class': 'form-control'}),
            'hours': forms.TextInput(attrs={'class': 'form-control'}),
            'game_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }