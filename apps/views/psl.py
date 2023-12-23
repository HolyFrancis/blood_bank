from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import PslForm, TypepslForm
from apps.models import PSL, Type_PSL, Blood
from apps.filters import PSLFilter

#TODO: Set calculation on durée de conservation and set default values for volume


def psl(request):
    psl = PSL.objects.all()
    types = Type_PSL.objects.all()
    filtre = PSLFilter(request.GET, queryset=psl)
    psl = filtre.qs
    
    context = {"psls": psl, "types":types, "filtre": filtre}

    return render(request, "apps/psl/psl.html", context)

def create_psl(request, id):
    blood = Blood.objects.get(id=id)
    
    of = request.GET.get("of")
    
    try:
        gr = Type_PSL.objects.get(name='GR')
        cps = Type_PSL.objects.get(name='CPS')
        pfc = Type_PSL.objects.get(name='PFC')
    except Type_PSL.DoesNotExist:
        messages.error(request, "Veuillez d'abord ajouter tous les types de produits sanguins labiles")
        return redirect(request.META.get('HTTP_REFERER'))
    
    if of == "gr":
        type_psl = Type_PSL.objects.get(name='GR')
    elif of == "pfc":
        type_psl = Type_PSL.objects.get(name='PFC')
    elif of == "cps":
        type_psl = Type_PSL.objects.get(name='CPS')
    form = PslForm(initial={'blood':blood,'type_psl':type_psl})
    
    if request.method == "POST":
        form = PslForm(request.POST)
        if form.is_valid():
            psl = form.save(commit=False)
            if of == 'gr':
                if psl.solution == None:
                    context = {"form": form, 'of':of}
                    messages.error(request, "Veuillez choisir une solution avant de continuer!")
                    return render(request, "apps/psl/create_psl.html", context)
                psl.duration = psl.solution.duration
                blood.gr = True
            elif of == "pfc":
                psl.duration = 365
                blood.pfc = True
            elif of == 'cps':
                psl.duration = 3
                blood.cps = True
            blood.save()
            psl.save()
            form.save_m2m()
            if blood.gr and blood.pfc and blood.cps:
                blood.centrifuged = True
                blood.save()
            item = request.POST
            if of == "gr":
                messages.success(request, "GR N°" + item['serial'] + " créé avec succès")
            elif of == "pfc":
                messages.success(request, "PFC N°" + item['serial'] + " créé avec succès")
            elif of == 'cps':
                messages.success(request, "CPS N°" + item['serial'] + " créé avec succès")
            return redirect("blood_request")
        else:
            psl = request.POST
            psls = PSL.objects.all()
            for p in psls:
                if p.serial == psl['serial']:
                    messages.error(request, p.serial + " existe déjà!")
            print(form.errors)
            
    context = {'form':form, 'of':of}
    
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
    blood = psl.blood
    
    context = {"psl":psl, "blood":blood}
    
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