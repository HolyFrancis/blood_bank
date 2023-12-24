from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.models import Client
from apps.forms.client import ClientForm

@login_required(login_url="login")
def client(request):
    clients = Client.objects.all()
    context = {"clients":clients}
    return render(request, "apps/client/client.html", context)

@login_required(login_url="login")
def create_client(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    context = {"form":form}
    return render(request, "apps/client/create_client.html", context)

@login_required(login_url="login")
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

@login_required(login_url="login")
def client_details(request, id):
    client = Client.objects.get(id=id)
    
    context = {"client":client}
    
    return render(request, "apps/client/client_details.html", context)

@login_required(login_url="login")
def delete_client(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    messages.success(request, "Le client supprimé avec succès!")
    
    context = {'client':client}
    
    return redirect('client')