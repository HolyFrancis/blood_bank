from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import PslForm, Type_pslForm
from apps.models import PSL, Type_psl


def psl(request):
    types_psl = Type_psl.objects.all()
    psl = PSL.objects.all()
    context = {"psls": psl, "types_psl": types_psl}

    return render(request, "apps/psl/psl.html", context)


def create_type_PSL(request):
    form = Type_pslForm()

    if request.method == "POST":
        form = Type_pslForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("psl")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "apps/psl/create_type_psl.html", context)


def update_type_psl(request, id):
    type_psl = Type_psl.objects.get(pk=id)
    form = Type_pslForm(instance=type_psl)

    if request.method == "POST":
        form = Type_pslForm(request.POST, instance=type_psl)
        if form.is_valid():
            form.save()
            return redirect("psl")
        else:
            print(form.errors)

    context = {"form": form, "type_psl": type_psl}

    return render(request, "apps/psl/create_type_psl.html", context)


def type_psl_details(request, id):
    type_psl = Type_psl.objects.get(id=id)
    context = {"psl": type_psl}

    return render(request, "apps/psl/psl_details", context)


def type_psl_delete(request, id):
    type_psl = Type_psl.objects.get(id=id)
    type_psl.delete()
    messages.success(request, "PSL type was deleted succesfully")

    return redirect("psl")


def create_psl(request):
    form = PslForm()

    if request.method == "POST":
        form = PslForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect("psl")
        else:
            return form.errors

    context = {"form": form, "psls": psl}

    return render(request, "apps/psl/create_psl.html", context)


def psl_details(request, id):
    psl = PSL.objects.get(id=id)

    context = {"psl": psl}
    return render(request, "apps/psl/psl_details.html", context)


def psl_delete(request, id):
    psl = PSL.objects.get(id=id)
    psl.delete()
    messages.success(request, "PSL deleted succesfully")

    return redirect("psl")
