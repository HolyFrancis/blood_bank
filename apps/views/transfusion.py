from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import BloodForm
from apps.models import Blood, Donor


def blood(request):
    accepted = Donor.objects.filter(status='Eligible')
    bloods = Blood.objects.all()
    
    context = {"bloods": bloods, "accepted":accepted}

    return render(request, "apps/transfusion/transfusion.html", context)


def create_blood(request, id):
    donor = Donor.objects.get(id=id)
    form = BloodForm(initial={'donor':donor})

    if request.method == "POST":
        form = BloodForm(request.POST)
        if form.is_valid():
            blood = request.POST
            form.save()
            messages.success(request, "La transfusion sanguine N°" + blood['serial'] + " a été enregistrée avec succès")
            return redirect('transfusion')
        else:
            current_blood = request.POST
            bloods = Blood.objects.all()
            for bl in bloods:
                if bl.serial == current_blood['serial']:
                    messages.error(request, "Le numéro de série saisi existe déjà!")
                elif bl.sample == current_blood['sample']:
                    messages.error(request, "L'échantillon saisi existe déjà!")
            print(form.errors)

    context = {"form": form}
    return render(request, "apps/transfusion/create_transfusion.html", context)


def update_blood(request, id):
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
        request, "apps/transfusion/create_transfusion.html", context={"form": form}
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
    bloods = Blood.objects.filter(centrifuged=False, analysed=True, state='Eligible').exclude(gr='True',pfc='True',cps='True')
    
    context = {"bloods": bloods}
    
    return render(request, "apps/transfusion/requests.html", context)

def blood_history(request):
    
    context = {}
    
    return render(request, "apps/transfusion/requests.html", context)