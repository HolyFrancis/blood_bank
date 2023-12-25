from django.shortcuts import render, redirect
from django.contrib import messages

from apps.forms import DonorForm
from apps.models import Donor

def public(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    form = DonorForm()
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            donor = request.POST
            messages.success(request, "Vous êtes désormais inscrit en tant que donneur potentiel. Votre requête sera étudiée. Vous recevrez plus d'instructions par email ou par messagerie")
            return redirect('home')
        else:
            donor = request.POST
            donors = Donor.objects.all()
            for don in donors:
                if don.cni == donor['cni']:
                    messages.error(request, "Un donneur avec la CNI saisie saisie existe déjà!")
    
    context = {'ingroups':ingroups, 'form':form}
    
    return render(request, "apps/public/index.html", context)