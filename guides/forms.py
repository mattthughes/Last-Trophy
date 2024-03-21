from django import forms
from trophy_hunter.models import Guide

class GuideForm(forms.ModelForm):
    """
    Form class for users to comment on a guide
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Guide
        fields = ('title','body','author')