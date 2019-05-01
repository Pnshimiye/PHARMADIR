from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PharmacyForm
from .models import Pharmacy
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url='/accounts/login/')
def view_pharmacy(request):
   current_user = request.user
   pharmacy = Pharmacy.objects.get(user = current_user.id)
   return render(request, 'profile.html',{'pharmacy':pharmacy})

def create_pharmacy(request):
  current_user = request.user
  if request.method == 'POST':
       form = PharmacyForm(request.POST, request.FILES)
       if form.is_valid():
           pharmacy = form.save(commit=False)
           pharmacy.user = current_user
           pharmacy.save()
       return render(request,'profile.html')
  else:
       form = PharmacyForm()
  return render(request, 'pharma-form.html', {"form": form})