from django import forms
from .models import Institute

class InstituteModelForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = '__all__'

        