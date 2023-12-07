from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import BloodForm
from apps.models import Blood


def blood(request):
    bloods = Blood.objects.all()

    return render(request, "apps/transfusion/transfusion.html", {"bloods": bloods})


def create_blood(request):
    form = BloodForm()

    if request.method == "POST":
        form = BloodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transfusion")

    context = {"form": form}
    return render(request, "apps/transfusion/create_transfusion.html", context)


def update_blood(request, id):
    blood = Blood.objects.get(pk=id)
    form = BloodForm(instance=blood)
    if request.method == "POST":
        form = BloodForm(request.POST, instance=blood)
        if form.is_valid():
            form.save()
            messages.success("blood has been updated succesfully")
            return redirect("transfusion")
        else:
            messages.error(request, "An error occured wile updating")

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
    messages.success(request, "the blood transfusion has been deleted succesfully")
    return redirect("transfusion")
