from django import forms
from trophy_hunter.models import Guide, Comment


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

class ApproveGuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('title', 'body', 'author', 'approved')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }