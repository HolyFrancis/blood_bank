from django.contrib import messages
from django.shortcuts import redirect, render

from apps.forms import ProductForm, ProductTypeForm
from apps.models import Product, ProductType


def equipement(request):
    products = Product.objects.all()
    productTypes = ProductType.objects.all()
    context = {"products": products, "productTypes": productTypes}

    return render(request, "apps/equipement/equipement.html", context)


def save_productType(request):
    form = ProductTypeForm()

    if request.method == "POST":
        form = ProductTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipement")

    context = {"form": form}
    return render(request, "apps/equipement/add_productType.html", context)


def update_productType(request, id):
    product_type = ProductType.objects.get(id=id)
    form = ProductTypeForm(instance=product_type)

    if request.method == "POST":
        form = ProductTypeForm(request.POST, instance=product_type)
        if form.is_valid():
            form.save()
        return redirect("equipement")

    context = {"form": form, "productType": product_type}

    return render(request, "apps/equipement/add_productType.html", context)


def productType_details(request, id):
    productType = ProductType.objects.get(id=id)
    context = {"productType": productType}

    return render(request, "apps/product/product_details", context)


def delete_productType(request, id):
    productType = ProductType.objects.get(id=id)
    productType.delete()
    messages.success(request, "the product type was deleted succesfully")

    return redirect("equipement")


def save_product(request):
    form = ProductForm()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipement")

    context = {"form": form}
    return render(request, "apps/equipement/add_equipement.html", context)


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("equipement")

    context = {"form": form, "product": product}
    return render(request, "apps/equipement/add_equipement.html", context)


def product_details(request, id):
    product = Product.objects.get(id=id)

    context = {"productType": product}
    return render(request, "apps/product/product_details", context)


def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, "the product was deleted succesfully")

    return redirect("equipement")
