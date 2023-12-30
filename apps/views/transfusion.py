from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from apps.forms import BloodForm
from apps.models import Blood, Donor
from apps.filters import BloodFilter

@login_required(login_url="login")
def blood(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    bloods = Blood.objects.all()
    bloods_count = bloods.all().count()
    eligible_bloods = bloods.filter(state='Eligible').count()
    ineligible_bloods = bloods.filter(state='Ineligible').count()
    pending_bloods = bloods.filter(state='Attente').count()

    eligible_bloods_percent = 0
    ineligible_bloods_percent = 0
    pending_bloods_percent = 0
    if eligible_bloods != 0:
        eligible_bloods_percent = eligible_bloods/bloods_count*100
        ineligible_bloods_percent = ineligible_bloods/bloods_count*100
        pending_bloods_percent = pending_bloods/bloods_count*100
    
    accepted = Donor.objects.filter(status='Eligible')
    filtre = BloodFilter(request.GET, queryset=bloods)
    bloods = filtre.qs
    
    context = {'ingroups':ingroups, 
        "bloods": bloods, 
        "accepted":accepted, 
        "filtre":filtre,
        'bloods_count':bloods_count,
        'eligible_bloods':eligible_bloods,
        'ineligible_bloods':ineligible_bloods,
        'pending_bloods':pending_bloods, 
        'eligible_bloods_percent':eligible_bloods_percent,
        'ineligible_bloods_percent':ineligible_bloods_percent,
        'pending_bloods_percent':pending_bloods_percent,
        }

    return render(request, "apps/transfusion/transfusion.html", context)

@login_required(login_url="login")
def create_blood(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    create = True
    donor = Donor.objects.get(id=id)
    form = BloodForm(initial={'donor':donor})

    if request.method == "POST":
        form = BloodForm(request.POST)
        if form.is_valid():
            blood = request.POST
            form.save()
            messages.success(request, "Le prélèvement N°" + blood['serial'] + " a été enregistré avec succès")
            return redirect('donor')
        else:
            current_blood = request.POST
            bloods = Blood.objects.all()
            for bl in bloods:
                if bl.serial == current_blood['serial']:
                    messages.error(request, "Le numéro de série saisi existe déjà!")
                elif bl.sample == current_blood['sample']:
                    messages.error(request, "L'échantillon saisi existe déjà!")
            print(form.errors)

    context = {'ingroups':ingroups, "form": form, "donor":donor, 'create':create}
    return render(request, "apps/transfusion/create_transfusion.html", context)

@login_required(login_url="login")
def update_blood(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    create = False
    blood = Blood.objects.get(pk=id)
    form = BloodForm(instance=blood)
    if request.method == "POST":
        form = BloodForm(request.POST, instance=blood)
        if form.is_valid():
            form.save()
            messages.success(request, "Le prélèvement N°" + blood.serial + " a été modifié avec succès")
            return redirect("transfusion")
        else:
            current_blood = request.POST
            bloods = Blood.objects.all()
            for bl in bloods:
                if bl.serial == current_blood['serial']:
                    messages.error(request, "Le numéro de série saisi existe déjà!")
                elif bl.sample == current_blood['sample']:
                    messages.error(request, "L'échantillon saisi existe déjà!")

    return render(
        request, "apps/transfusion/create_transfusion.html", context={'ingroups':ingroups,"form": form, 'create':create}
    )

@login_required(login_url="login")
def blood_details(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    blood = Blood.objects.get(pk=id)
    return render(
        request, "apps/transfusion/transfusion_details.html", {'ingroups':ingroups,"blood": blood}
    )

@login_required(login_url="login")
def blood_delete(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    blood = Blood.objects.get(pk=id)
    blood.delete()
    messages.success(request, "Le prélèvement a été supprimé avec succès")
    return redirect("transfusion")

@login_required(login_url="login")
def blood_request(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    bloods = Blood.objects.filter(centrifuged=False, analysed=True, state='Eligible').exclude(gr=True, pfc=True, cps=True)
    
    context = {'ingroups':ingroups, "bloods": bloods}
    
    return render(request, "apps/transfusion/requests.html", context)

@login_required(login_url="login")
def blood_history(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    centrifuged = Blood.objects.filter(centrifuged=True)
    
    blood_psls={}
    
    context = {'ingroups':ingroups, 'centrifuged':centrifuged, 'blood_psls':blood_psls}
    
    return render(request, "apps/transfusion/history.html", context)