from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import PslForm, TypepslForm
from apps.models import PSL, Type_PSL

#TODO: Set calculation on durée de conservation and set default values for volume


def psl(request):
    psl = PSL.objects.all()
    types = Type_PSL.objects.all()
    context = {"psls": psl, "types":types}

    return render(request, "apps/psl/psl.html", context)


def create_psl(request):
    form = PslForm()

    if request.method == "POST":
        form = PslForm(request.POST)
        if form.is_valid():
            psl = form.save(commit=False)
            if psl.type_psl.name == "GR":
                if psl.solution == None:
                    context = {"form": form}
                    messages.error(request, "Veuillez choisir une solution avant de continuer!")
                    return render(request, "apps/psl/create_psl.html", context)
                psl.duration = psl.solution.duration
            elif psl.type_psl.name == "PFC":
                psl.duration = 365
                if psl.solution != None:
                    context = {"form": form}
                    messages.error(request, "Un PSL de type PFC n'est mélangé avec aucune solution!")
                    return render(request, "apps/psl/create_psl.html", context)
            elif psl.type_psl.name == "CPS":
                psl.duration = 3
                if psl.solution != None:
                    context = {"form": form}
                    messages.error(request, "Un PSL de type CPS n'est mélangé avec aucune solution!")
                    return render(request, "apps/psl/create_psl.html", context)
            psl.save()
            form.save_m2m()
            item = request.POST
            messages.success(request, item['serial'] + " créé avec succès")
            return redirect("psl")
        else:
            psl = request.POST
            psls = PSL.objects.all()
            for p in psls:
                if p.serial == psl['serial']:
                    messages.error(request, p.serial + " existe déjà!")
            print(form.errors)

    context = {"form": form}
    return render(request, "apps/psl/create_psl.html", context)


def update_psl(request, id):
    psl = PSL.objects.get(id=id)

    form = PslForm(instance=psl)

    if request.method == "POST":
        form = PslForm(request.POST, instance=psl)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['serial'] + " modifié avec succès")
            return redirect("psl")
        else:
            return form.errors

    context = {"form": form, "psls": psl}

    return render(request, "apps/psl/create_psl.html", context)


def psl_details(request, id):
    psl = PSL.objects.get(id=id)
    bloods = psl.blood.all()
    
    context = {"psl":psl, "bloods":bloods}
    
    return render(request, "apps/psl/psl-details.html", context)

def psl_delete(request, id):
    psl = PSL.objects.get(id=id)
    psl.delete()
    messages.success(request, "PSL supprimé avec succès")

    return redirect("psl")


def create_type(request):
    form = TypepslForm()

    if request.method == "POST":
        form = TypepslForm(request.POST)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " Enregistré avec succès")
            return redirect("psl")
        else:
            typ = request.POST
            types = Type_PSL.objects.all()
            for ty in types:
                if ty.name == typ['name']:
                    messages.error(request, typ['name'] + " existe déjà!")
            print(form.errors)
    
    context = {"form": form}
    return render(request, "apps/psl/create_type.html", context)
    
            
def update_type(request, id):
    typ = Type_PSL.objects.get(id=id)
    
    form = TypepslForm(instance=typ)

    if request.method == "POST":
        form = TypepslForm(request.POST, instance=typ)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " Modifié avec succès")
            return redirect("psl")
        else:
            typ = request.POST
            types = Type_PSL.objects.all()
            for ty in types:
                if ty.name == typ['name']:
                    messages.error(request, ty.name + " existe déjà!")
            print(form.errors)
    
    context = {"form": form}
    return render(request, "apps/psl/create_type.html", context)


def delete_type(request, id):
    typ = Type_PSL.objects.get(id=id)
    typ.delete()
    messages.success(request, "Type de PSL supprimé avec succès")

    return redirect("psl")