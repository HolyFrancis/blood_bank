from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages

from apps.models import Client
from apps.forms.client import ClientForm

def client(request):
    clients = Client.objects.all()
    context = {"clients":clients}
    return render(request, "apps/client/client.html", context)

def create_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    context = {"form":form}
    return render(request, "apps/client/create_client.html", context)

def update_client(request, id):
    client = Client.objects.get(id=id)
    
    form = ClientForm(instance=client)
    
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
        else:
            return form.errors
    
    context = {"form":form, 'client':client}
    
    return render(request, "apps/client/create_client.html", context)



def client_details(request, id):
    client = Client.objects.get(id=id)
    
    context = {"client":client}
    
    return render(request, "apps/client/client_details.html", context)

def delete_client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    messages.success(request, "Dlient deleted successefuly!")
    
    context = {'client':client}
    
    return redirect('client')