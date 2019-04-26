from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Medicine, Pharmacy,Request
from django.contrib.auth.models import User
from .forms import MedicineForm, PharmacyForm, RequestForm
 
def post_request(request):    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if  form.is_valid():
            upload = form.save(commit=False)
            # upload.profile = current_user           
            # upload.save()
            return redirect('home')
  
    else:
        form =RequestForm()
    
    return render(request, 'account_request_form.html', {'form':form})

def home(request): 
    title = 'Home' 
   
    return render(request, 'home.html', {'title':title})
