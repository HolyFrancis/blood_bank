from django.shortcuts import render, redirect
from django.contrib import messages

from apps.forms import DonorForm
from apps.models import Donor, Users


def public(request):

    form = DonorForm()
    if request.method == "POST":
        form = DonorForm(request.POST)
        print(f"FORM IS VALID {form.is_valid()}")
        if form.is_valid():
            donor = form.save()
            # donor = request.POST
            user = Users.objects.create(username=form.cleaned_data["username"], email=form.cleaned_data["email"], first_name=form.cleaned_data["first_name"], last_name=form.cleaned_data["last_name"])
            print(f"USER ===={user}")
            user.set_password(form.cleaned_data["password"])
            user.donor = donor
            user.save()
            messages.success(request, "Vous êtes désormais inscrit en tant que donneur potentiel. Votre requête sera étudiée. Vous recevrez plus d'instructions par email ou par messagerie")
            return redirect("login")
        else:
            donor = request.POST
            donors = Donor.objects.all()
            for don in donors:
                if don.cni == donor["cni"]:
                    messages.error(request, "Un donneur avec la CNI saisie saisie existe déjà!")

    context = {"form": form}

    return render(request, "apps/public/index.html", context)
