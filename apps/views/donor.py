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
            donor = request.POST
            messages.success(request, donor['first_name'] + ' ' + donor['last_name'] + " ajouté avec succès")
            return redirect('donor')
        else:
            donor = request.POST
            donors = Donor.objects.all()
            for don in donors:
                if don.cni == donor['cni']:
                    messages.error(request, "La CNI saisie existe déjà!")
    
    context = {"form":form}
    
    return render(request, "apps/donor/create_donor.html", context)

def update_donor(request, id):
    donor = Donor.objects.get(id=id)
    
    form = DonorForm(instance=donor)
    
    if request.method == "POST":
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            donor = request.POST
            messages.success(request, donor['first_name'] + ' ' + donor['last_name'] + " modifié avec succès")
            return redirect('donor')
        else:
            donor = request.POST
            donors = Donor.objects.all()
            for don in donors:
                if don.cni == donor['cni']:
                    messages.error(request, "La CNI saisie existe déjà!")
    
    context = {"form":form, 'donor':donor}
    
    return render(request, "apps/donor/create_donor.html", context)

def donor_details(request, id):
    donor = Donor.objects.get(id=id)
    
    context = {"donor":donor}
    
    return render(request, "apps/donor/donor_details.html", context)

def delete_donor(request, id):
    donor = Donor.objects.get(id=id)
    donor.delete()
    messages.success(request, "Donneur supprimer avec succès!")
    
    context = {'donor':donor}
    
    return redirect('donor')

def donor_requests(request):
    donors = Donor.objects.filter(status='Attente')
    
    context = {'donors':donors}
    
    return render(request, "apps/donor/requests.html", context)

def request_decision(request, id):
    donor = Donor.objects.get(id=id)
    q = request.GET.get("q")
    if q=='confirm':
        donor.status = 'Eligible'
        donor.save()
        messages.success(request, donor.first_name + ' ' + donor.last_name + " désormais éligible au don de sang")
    elif q=="reject":
        donor.status = 'Ineligible'
        donor.save()
        messages.warning(request, donor.first_name + ' ' + donor.last_name + " désormais inéligible au don de sang")
    return redirect('donor_requests')
    
def donor_history(request):
    accepted = Donor.objects.filter(status='Eligible')
    refused = Donor.objects.filter(status='Ineligible')
    
    context = {'accepted':accepted, 'refused':refused}
    
    return render(request, "apps/donor/history.html", context)
    