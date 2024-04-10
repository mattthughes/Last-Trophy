from django import forms
from trophy_hunter.models import Game, Trophies


class GameForm(forms.ModelForm):
    """
    Form class for users to create a guide
    """
    class Meta:
        model = Game
        fields = (
            'title',
            'slug',
            'featured_image',
            'genre',
            'trophy_count',
            'hours',
            'rating')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'trophy_count': forms.TextInput(attrs={'class': 'form-control'}),
            'hours': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TrophiesForm(forms.ModelForm):
    """
    Form class for users to create a trophy
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Trophies
        fields = (
            'title',
            'slug',
            'featured_image',
            'description',
            'difficulty',
            'rarity')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'difficulty': forms.TextInput(attrs={'class': 'form-control'}),
            'rarity': forms.NumberInput(attrs={'class': 'form-control'}),
        }