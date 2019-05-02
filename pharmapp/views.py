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
 
 
def post_request(request):    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if  form.is_valid():
            post = form.save(commit=False)                    
            post.save()
            name = form.cleaned_data['pharmacy']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('home')
            return redirect('home')
  
    else:
        form =RequestForm()
    messages.info(request, 'Your request has been posted successfully. Please while out team review it, we will get back to you in the next 24 hours')
    
    return render(request, 'account_request_form.html', {'form':form})

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
    # medicines = Medicine.get_pharmacy_medicines(pharmacy.user_id)
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


@login_required(login_url = '/accounts/login/')
def search_pharmacy(request):

    if 'medicine' in request.GET and request.GET["medicine"]:
        search_term = request.GET.get("medicine")
        # print(search_term)
        # medicine = Medicine.objects.get(name=search_term)
        print(medicine)
        print(search_term)

        searched_pharmacy = Pharmacy.get_pharmacies_with_medicine(medicine)
        print(searched_pharmacy)
        message = f"{search_term}"

        return render(request, 'search_pharmacy.html',{"message":message,"pharmacy": searched_pharmacy})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_pharmacy.html',{"message":message})



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


class SearchView(ListView):
    template_name = 'lookup.html'
    paginate_by = 20
    count = 0
    
def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['count'] = self.count or 0
    context['query'] = self.request.GET.get('q')
    return context

def get_queryset(self):
    request = self.request
    query = request.GET.get('q', None)
    
    if query is not None:
        blog_results        = Post.objects.search(query)
        lesson_results      = Lesson.objects.search(query)
        profile_results     = Profile.objects.search(query)
        
        # combine querysets 
        queryset_chain = chain(
                blog_results,
                lesson_results,
                profile_results
        )        
        qs = sorted(queryset_chain, 
                    key=lambda instance: instance.pk, 
                    reverse=True)
        self.count = len(qs) 
        return qs
    return Post.objects.none() #