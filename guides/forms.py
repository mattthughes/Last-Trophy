from django import forms
from trophy_hunter.models import Guide

class GuideForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Guide
        fields = ('body',)