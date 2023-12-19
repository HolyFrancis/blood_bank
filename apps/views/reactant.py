from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import ReactantForm
from apps.models import Reactant


def reactant(request):
    reactants = Reactant.objects.all()
    context = {"reactants": reactants}

    return render(request, "apps/reactant/reactant.html", context)

def save_reactant(request):
    form = ReactantForm()

    if request.method == "POST":
        form = ReactantForm(request.POST)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " ajouté avec succès")
            return redirect("reactant")

    context = {"form": form}
    return render(request, "apps/reactant/add_reactant.html", context)


def update_reactant(request, id):
    reactant = Reactant.objects.get(id=id)
    form = ReactantForm(instance=reactant)

    if request.method == "POST":
        form = ReactantForm(request.POST, instance=reactant)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " modifié avec succès")
        return redirect("reactant")

    context = {"form": form, "reactant": reactant}
    return render(request, "apps/reactant/add_reactant.html", context)


def delete_reactant(request, id):
    reactant = Reactant.objects.get(id=id)
    reactant.delete()
    messages.success(request, "Réactif supprimé avec succès")

    return redirect("reactant")
