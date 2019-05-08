from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Medicine, Pharmacy,Request,Insurance
from django.contrib.auth.models import User
from .forms import MedicineForm, PharmacyForm, RequestForm,InsuranceForm
from django.contrib import messages
from .email import send_welcome_email
from itertools import chain
from django.views.generic import ListView
from .email import send_welcome_email
 
def post_request(request):    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if  form.is_valid():
            request = form.save(commit=False)
            request.save()
            name = request.Pharmacy_name
            email = request.Contact_Email
            send_welcome_email(name, email)
            HttpResponseRedirect('home')
            return redirect('home')
  
    else:
        form =RequestForm()
    return render(request, 'account_request_form.html',{'form':form})
    
def home(request): 
    title = 'Home' 
    pharmacy = Pharmacy.objects.filter()
    return render(request, 'index.html', {'title':title})


@login_required(login_url='/accounts/login/')
def view_pharmacy(request):
    current_user = request.user
    pharmacy = Pharmacy.objects.get(user = current_user.id)
    medicines =  Medicine.objects.filter(pharmacy=pharmacy)
    insurances = Insurance.objects.filter(pharmacy=pharmacy)
    print(insurances)   
    return render(request, 'profile.html',{'pharmacy':pharmacy,'medicines':medicines,'insurances':insurances})


@login_required(login_url='/accounts/login/')
def create_pharmacy(request):
   current_user = request.user
   if request.method == 'POST':
        form = PharmacyForm(request.POST, request.FILES)
        if form.is_valid():
            pharmacy = form.save(commit=False)
            pharmacy.user = current_user
            pharmacy.save()
        return redirect('view_pharmacy')
   else:
        form = PharmacyForm()
   return render(request, 'pharma-form.html', {"form": form})


 
def search_pharmacy(request):

    if 'medicine' in request.GET and request.GET["medicine"]:
        search_term = request.GET.get("medicine")     
        medicine = Medicine.objects.filter(name=search_term).all()       
        searched_pharmacy = None      
        for i in medicine:
            searched_pharmacy = Pharmacy.get_pharmacies_with_medicine(i.pharmacy.id)          
        message = f"{search_term}"
        return render(request, 'search_pharmacy.html',{"message":message,"pharmacy": searched_pharmacy})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search_pharmacy.html',{"message":message})

 
def search_pharmacy_insurance(request):
    print("ok")
    if 'insurance' in request.GET and request.GET["insurance"]:
        search_term2 = request.GET.get("insurance")        
        insurance = Insurance.objects.filter(name=search_term2).all()        
        searched_pharmacy = None
        print(insurance)
        for i in insurance:
            searched_pharmacy = Pharmacy.get_pharmacies_with_medicine(i.pharmacy.id)        
        print(searched_pharmacy)
        message = f"{search_term2}"


        return render(request, 'search_insurance.html',{"message":message,"pharmacy": searched_pharmacy})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_insurance.html',{"message":message})


@login_required(login_url='/accounts/login/')
def create_insurances(request):
   current_user = request.user
   pharmacy= Pharmacy.objects.get(user=current_user)
   if request.method == 'POST':
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            insurances = form.save(commit=False)
            insurances.pharmacy = pharmacy
            insurances.save()
        return redirect('view_pharmacy')
   else:
        form = InsuranceForm()
   return render(request, 'insurance-form.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_insurances(request):
    current_user = request.user
    insurances = Insurance.objects.get(user = current_user.id)
    return render(request, 'profile.html',{'pharmacy':pharmacy})

@login_required(login_url='/accounts/login/')
def create_medecines(request):
   current_user = request.user
   pharmacy= Pharmacy.objects.get(user=current_user)
   if request.method == 'POST':
        form = MedicineForm(request.POST, request.FILES)
        if form.is_valid():
            medicines = form.save(commit=False)
            medicines.pharmacy = pharmacy
            medicines.save()
        return redirect('view_pharmacy')
   else:
        form = MedicineForm()
   return render(request, 'medicines.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_medecines(request):
    current_user = request.user
    medicines = Medicine.objects.get(user = current_user.id)
   
    return render(request, 'profile.html',{'pharmacy':pharmacy})