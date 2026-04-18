from django import forms
from .models import HealthTip

# class HealthTipForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     content = forms.CharField(widget=forms.Textarea)  <-- We're no longer using this

class HealthTipForm(forms.ModelForm):
    class Meta:
        model = HealthTip
        fields = ['title', 'content']