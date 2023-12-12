from django.shortcuts import redirect, render
from apps.models import Stock,Location
from django.contrib import messages
from apps.forms.stock import StockForm
from apps.forms.location import LocationForm

def stock(request):
    stocks=Stock.objects.all()
    locations=Location.objects.all()
    context = {"stocks":stocks,"locations":locations}
    return render(request, "apps/stock/stock.html", context)

def create_stock(request):
    form = StockForm()
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock')
    context = {"form":form}
    return render(request, "apps/stock/create_stock.html", context)

def create_location(request):
    form = LocationForm()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock')
    context = {"form":form}
    return render(request, "apps/stock/create_location.html", context)

def update_stock(request, id):
    stock = Stock.objects.get(id=id)
    
    form = StockForm(instance=stock)
    
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
        else:
            return form.errors
    
    context = {"form":form, 'stock':stock}
    
    return render(request, "apps/stock/create_stock.html", context)

def update_location(request, id):
    locations = Location.objects.get(id=id)
    
    form = LocationForm(instance=locations)
    
    if request.method == "POST":
        form = LocationForm(request.POST, instance=locations)
        if form.is_valid():
            form.save()
            return redirect('stock')
        else:
            return form.errors
    
    context = {"form":form, 'locations':locations}
    
    return render(request, "apps/stock/create_location.html", context)


def delete_stock(request, id):
    stock = Stock.objects.get(id=id)
    stock.delete()
    messages.success(request, "Le stock a été supprimé avec succès!")
    
    context = {'stock':stock}
    
    return redirect('stock')


def delete_location(request, id):
    location = Location.objects.get(id=id)
    location.delete()
    messages.success(request, "L'emplassement a été supprimé avec succès!")
    
    context = {'location':location}
    
    return redirect('stock')

