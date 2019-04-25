from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def pharmacy(request):
   current_user = request.user
   if request.method == 'POST':
        form = PharmacyForm(request.POST, request.FILES)
        if form.is_valid():
            pharmacy = form.save(commit=False)
            pharmacy.editor = current_user
            pharmacy.save()
        return redirect('pharmacy')
   else:
        form = PharmacyForm()
   return render(request, 'pharma-form.html', {"form": form})