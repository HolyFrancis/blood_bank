from django.shortcuts import redirect, render
from django.contrib import messages

from apps.models import Donor
from apps.forms import DonorForm
from apps.filters import DonorFilter


def donor(request):
    donors_count = Donor.objects.all().count()
    eligible_donors = Donor.objects.filter(status = 'Eligible').count()
    ineligible_donors = Donor.objects.filter(status='Ineligible').count()
    pending_donors = Donor.objects.filter(status='Attente').count()

    eligible_donors_percent = 0
    ineligible_donors_percent = 0
    pending_donors_percent = 0
    if donors_count is not 0:
        eligible_donors_percent = eligible_donors/donors_count*100
        ineligible_donors_percent = ineligible_donors/donors_count*100
        pending_donors_percent = pending_donors/donors_count*100
    
    donors = Donor.objects.all()
    filtre = DonorFilter(request.GET, queryset=donors)
    donors = filtre.qs
    
    context = {
        "donors":donors, 
        "filtre":filtre,
        'donors_count':donors_count,
        'eligible_donors':eligible_donors,
        'ineligible_donors':ineligible_donors,
        'pending_donors':pending_donors,
        'eligible_donors_percent':eligible_donors_percent, 'ineligible_donors_percent':ineligible_donors_percent,'pending_donors_percent':pending_donors_percent,
        }
    
    return render(request, "apps/donor/donor.html", context)

def create_donor(request):
    create = True
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
                    messages.error(request, "Un donneur avec la CNI saisie saisie existe déjà!")
    
    context = {
        "form":form,
        "create":create
        }
    
    return render(request, "apps/donor/create_donor.html", context)

def update_donor(request, id):
    create = False
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
    
    context = {"form":form, 'donor':donor, 'create':create}
    
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
        messages.success(request, donor.first_name + ' ' + donor.last_name + " désormais éligible aux dons de sang")
    elif q=="reject":
        donor.status = 'Ineligible'
        donor.save()
        messages.warning(request, donor.first_name + ' ' + donor.last_name + " désormais inéligible aux dons de sang")
    waiting_donors = Donor.objects.filter(status='Attente')
        
    if waiting_donors.count() == 0:
        return redirect("donor")
    
    return redirect('donor_requests')
    
def donor_history(request):
    accepted = Donor.objects.filter(status='Eligible')
    refused = Donor.objects.filter(status='Ineligible')
    
    context = {'accepted':accepted, 'refused':refused}
    
    return render(request, "apps/donor/history.html", context)
    