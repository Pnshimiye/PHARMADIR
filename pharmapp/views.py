from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Medicine, Pharmacy,Request
from django.contrib.auth.models import User
from .forms import MedicineForm, PharmacyForm, RequestForm
 
