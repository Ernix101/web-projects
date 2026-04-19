from django import forms
from .models import GymTip

# class GymTipForm(forms.Form):
    # title = forms.CharField(max_length=255)
    # description = forms.CharField(widget=forms.Textarea)

class GymTipForm(forms.ModelForm):
    class Meta:
        model = GymTip
        fields = ['title', 'description']
