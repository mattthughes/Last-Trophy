from django import forms

class GameNameFilterForm(forms.Form):
    title = forms.CharField()