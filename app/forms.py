from django import forms
from .models import Player

class PlayerAddForm(forms.ModelForm):
    class Meta:
        model=Player
        fields=['first_name','middle_name','last_name','country','club']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','id':'firstnameid'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'middlenameid'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastnameid'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'id': 'countryid'}),
            'club': forms.TextInput(attrs={'class': 'form-control', 'id': 'clubid'}),
        }