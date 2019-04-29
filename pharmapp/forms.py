from django import forms
from django.core.files import File
from .models import Pharmacy


class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        exclude = []
