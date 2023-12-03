from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages

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

def update_donor(request, id):
    donor = Donor.objects.get(id=id)
    
    form = DonorForm(instance=donor)
    
    if request.method == "POST":
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor')
        else:
            return form.errors
    
    context = {"form":form, 'donor':donor}
    
    return render(request, "apps/donor/create_donor.html", context)

def donor_details(request, id):
    donor = Donor.objects.get(id=id)
    
    context = {"donor":donor}
    
    return render(request, "apps/donor/donor_details.html", context)

def delete_donor(request, id):
    donor = Donor.objects.get(id=id)
    donor.delete()
    messages.success(request, "Donor deleted successefuly!")
    
    context = {'donor':donor}
    
    return redirect('donor')