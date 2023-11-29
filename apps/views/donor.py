from django.shortcuts import redirect, render

from apps.models import Donor
from apps.forms import DonorForm

def donor(request):
    donors = Donor.objects.all()
    
    context = {"donors":donors}
    
    return render(request, "apps/donor/donor.html", context)

def create_donor(request):
    form = DonorForm()
    
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor')
    
    context = {"form":form}
    
    return render(request, "apps/donor/create_donor.html", context)