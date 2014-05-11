from django import forms

from .models import FloodingWarning


class FloodingWarningForm(forms.ModelForm):
    class Meta:
        model = FloodingWarning
