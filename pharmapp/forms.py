from django import forms
from django.contrib.auth.models import User
from .models import Pharmacy,Request,Medicine,Insurance





class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['Request_date']

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        exclude = ['user']
     

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        exclude = ['pharmacy']

class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        exclude = ['pharmacy']

     