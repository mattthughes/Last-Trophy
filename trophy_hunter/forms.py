from django import forms

class GameNameFilterForm(forms.Form):
    name = forms.CharField()