from django import forms
from trophy_hunter.models import Guide


class GuideForm(forms.ModelForm):
    """
    Form class for users to create a guide
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Guide
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
