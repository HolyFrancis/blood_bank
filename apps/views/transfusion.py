from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import BloodForm
from apps.models import Blood, Donor
from apps.filters import BloodFilter


def blood(request):
    bloods = Blood.objects.all()
    bloods_count = bloods.all().count()
    eligible_bloods = bloods.filter(state='Eligible').count()
    ineligible_bloods = bloods.filter(state='Ineligible').count()
    pending_bloods = bloods.filter(state='Attente').count()

    eligible_bloods_percent = 0
    ineligible_bloods_percent = 0
    pending_bloods_percent = 0
    if eligible_bloods is not 0:
        eligible_bloods_percent = eligible_bloods/bloods_count*100
        ineligible_bloods_percent = ineligible_bloods/bloods_count*100
        pending_bloods_percent = pending_bloods/bloods_count*100
    
    accepted = Donor.objects.filter(status='Eligible')
    filtre = BloodFilter(request.GET, queryset=bloods)
    bloods = filtre.qs
    
    context = {
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


def create_blood(request, id):
    create = True
    donor = Donor.objects.get(id=id)
    form = BloodForm(initial={'donor':donor})

    if request.method == "POST":
        form = BloodForm(request.POST)
        if form.is_valid():
            blood = request.POST
            form.save()
            messages.success(request, "La transfusion sanguine N°" + blood['serial'] + " a été enregistrée avec succès")
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

    context = {"form": form, "donor":donor, 'create':create}
    return render(request, "apps/transfusion/create_transfusion.html", context)


def update_blood(request, id):
    create = False
    blood = Blood.objects.get(pk=id)
    form = BloodForm(instance=blood)
    if request.method == "POST":
        form = BloodForm(request.POST, instance=blood)
        if form.is_valid():
            form.save()
            messages.success(request, "La transfusion sanguine N°" + blood.serial + " a été modifiée avec succès")
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
        request, "apps/transfusion/create_transfusion.html", context={"form": form, 'create':create}
    )


def blood_details(request, id):
    blood = Blood.objects.get(pk=id)
    return render(
        request, "apps/transfusion/transfusion_details.html", {"blood": blood}
    )


def blood_delete(request, id):
    blood = Blood.objects.get(pk=id)
    blood.delete()
    messages.success(request, "La transfusion sanguine a été supprimée avec succès")
    return redirect("transfusion")


def blood_request(request):
    bloods = Blood.objects.filter(centrifuged=False, analysed=True, state='Eligible').exclude(gr=True, pfc=True, cps=True)
    
    context = {"bloods": bloods}
    
    return render(request, "apps/transfusion/requests.html", context)

def blood_history(request):
    centrifuged = Blood.objects.filter(centrifuged=True)
    
    blood_psls={}
    
    for blood in centrifuged:
        for psl in blood.psl_set.all():
            blood_psls.update({psl:blood})
    
    context = {'centrifuged':centrifuged, 'blood_psls':blood_psls}
    
    return render(request, "apps/transfusion/history.html", context)