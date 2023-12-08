from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import EquipmentForm, EquipmentTypeForm
from apps.models import Equipment, EquipmentType


def equipement(request):
    equipments = Equipment.objects.all()
    equipmentTypes = EquipmentType.objects.all()
    context = {"equipments": equipments, "equipmentTypes": equipmentTypes}

    return render(request, "apps/equipement/equipement.html", context)


def save_equipmentType(request):
    form = EquipmentTypeForm()

    if request.method == "POST":
        form = EquipmentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipement")

    context = {"form": form}
    return render(request, "apps/equipement/add_equipmentType.html", context)


def update_equipmentType(request, id):
    equipment_type = EquipmentType.objects.get(id=id)
    form = EquipmentTypeForm(instance=equipment_type)

    if request.method == "POST":
        form = EquipmentTypeForm(request.POST, instance=equipment_type)
        if form.is_valid():
            form.save()
        return redirect("equipement")

    context = {"form": form, "equipmentType": equipment_type}

    return render(request, "apps/equipement/add_equipmentType.html", context)


def equipmentType_details(request, id):
    equipmentType = EquipmentType.objects.get(id=id)
    context = {"equipmentType": equipmentType}

    return render(request, "apps/equipment/equipment_details", context)


def delete_equipmentType(request, id):
    equipmentType = EquipmentType.objects.get(id=id)
    equipmentType.delete()
    messages.success(request, "the equipment type was deleted succesfully")

    return redirect("equipement")


def save_equipment(request):
    form = EquipmentForm()

    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipement")

    context = {"form": form}
    return render(request, "apps/equipement/add_equipement.html", context)


def update_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    form = EquipmentForm(instance=equipment)

    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
        return redirect("equipement")

    context = {"form": form, "equipment": equipment}
    return render(request, "apps/equipement/add_equipement.html", context)


def equipment_details(request, id):
    equipment = Equipment.objects.get(id=id)

    context = {"equipmentType": equipment}
    return render(request, "apps/equipment/equipment_details", context)


def delete_equipment(request, id):
    equipment = Equipment.objects.get(id=id)
    equipment.delete()
    messages.success(request, "the equipment was deleted succesfully")

    return redirect("equipement")
