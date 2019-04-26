from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PharmacyForm
from .models import Pharmacy
# Create your views here.

@login_required(login_url='/accounts/login/')
def profile(request):
  pharmacy = Pharmacy.objects.get()
  return render(request, 'profile.html',{'pharmacy':pharmacy})

def pharmacy(request):
   current_user = request.user
   if request.method == 'POST':
        form = PharmacyForm(request.POST, request.FILES)
        if form.is_valid():
            pharmacy = form.save(commit=False)
            pharmacy.editor = current_user
            pharmacy.save()
        return redirect('profile')
   else:
        form = PharmacyForm()
   return render(request, 'pharma-form.html', {"form": form})

