from django import forms
from .models import ApplicantsData


class AppylForm(forms.ModelForm):
    class Meta:
        model = ApplicantsData
        fields = ['name', 'email', 'website', 'cv', 'cover_latter']
