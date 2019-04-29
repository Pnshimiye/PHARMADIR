from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Medicine, Pharmacy,Request
from django.contrib.auth.models import User
from .forms import MedicineForm, PharmacyForm, RequestForm
from django.contrib import messages
 
 
def post_request(request):    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if  form.is_valid():
            post = form.save(commit=False)                    
            post.save()
            return redirect('home')
  
    else:
        form =RequestForm()
    messages.info(request, 'Your password has been changed successfully!')
    
    return render(request, 'account_request_form.html', {'form':form})

def home(request): 
    title = 'Home' 
   
    return render(request, 'index.html', {'title':title})


@login_required(login_url='/accounts/login/')
def view_pharmacy(request):
  pharmacy = Pharmacy.objects.get()
  return render(request, 'profile.html',{'pharmacy':pharmacy})

def create_pharmacy(request):
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
