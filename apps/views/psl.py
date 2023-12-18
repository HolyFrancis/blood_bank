from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import PslForm, PriceForm
from apps.models import PSL, Price

#TODO: Set calculation on durée de conservation and set default values for volume


def psl(request):
    psl = PSL.objects.all()
    context = {"psls": psl}

    return render(request, "apps/psl/psl.html", context)


def create_psl(request):
    form = PslForm()

    if request.method == "POST":
        form = PslForm(request.POST)
        if form.is_valid():
            psl = form.save(commit=False)
            psl.price = Price.objects.get(typ=psl.typ)
            if psl.typ == "GR":
                if psl.solution == None:
                    context = {"form": form}
                    messages.error(request, "Veuillez choisir une solution avant de continuer!")
                    return render(request, "apps/psl/create_psl.html", context)
                psl.duration = psl.solution.duration
            elif psl.typ == "PFC":
                psl.duration = 365
                if psl.solution != None:
                    context = {"form": form}
                    messages.error(request, "Un PSL de type PFC n'est mélangé avec aucune solution!")
                    return render(request, "apps/psl/create_psl.html", context)
            elif psl.typ == "CPS":
                psl.duration = 3
                if psl.solution != None:
                    context = {"form": form}
                    messages.error(request, "Un PSL de type CPS n'est mélangé avec aucune solution!")
                    return render(request, "apps/psl/create_psl.html", context)
            psl.save()
            item = request.POST
            messages.success(request, item['serial'] + " créé avec succès")
            return redirect("psl")
        else:
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


def psl_delete(request, id):
    psl = PSL.objects.get(id=id)
    psl.delete()
    messages.success(request, "PSL supprimé avec succès")

    return redirect("psl")


def price(request):
    prices = Price.objects.all()
    context = {"prices": prices}

    return render(request, "apps/psl/price.html", context)


def create_price(request):
    form = PriceForm()

    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['typ'] + ":" +item['price'] + " Enregistré avec succès")
            return redirect("price")
        else:
            price = request.POST
            prices = Price.objects.all()
            for pri in prices:
                if pri.typ == price['typ']:
                    messages.error(request, "Un prix pour " + pri.typ + " existe déjà!")
            print(form.errors)
    
    context = {"form": form}
    return render(request, "apps/psl/create_price.html", context)
    
            
def update_price(request, id):
    price = Price.objects.get(id=id)
    
    form = PriceForm(instance=price)

    if request.method == "POST":
        form = PriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['typ'] + ":" +item['price'] + " Modifié avec succès")
            return redirect("price")
        else:
            price = request.POST
            prices = Price.objects.all()
            for pri in prices:
                if pri.typ == price['typ']:
                    messages.error(request, "Un prix pour " + pri.typ + " existe déjà!")
            print(form.errors)
    
    context = {"form": form}
    return render(request, "apps/psl/create_price.html", context)


def delete_price(request, id):
    price = Price.objects.get(id=id)
    price.delete()
    messages.success(request, "Prix supprimé avec succès")

    return redirect("price")