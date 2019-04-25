from django import forms
from django.core.files import File
from .models import Pharmacy


class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        exclude = []

# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like
#         exclude = ['user']

# class SubscriptionForm(forms.ModelForm):
#     email = forms.EmailField(label='Email')