from django import forms

from main_module.models import Audio


class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ["audio"]
