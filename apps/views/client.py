from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.models import Client
from apps.forms.client import ClientForm

@login_required(login_url="login")
def client(request):
    ingroups = request.user.groups.exists()
    clients = Client.objects.all()
    context = {'ingroups':ingroups, "clients":clients}
    return render(request, "apps/client/client.html", context)

@login_required(login_url="login")
def create_client(request):
    ingroups = request.user.groups.exists()
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
    context = {'ingroups':ingroups, "form":form}
    return render(request, "apps/client/create_client.html", context)

@login_required(login_url="login")
def update_client(request, id):
    ingroups = request.user.groups.exists()
    client = Client.objects.get(id=id)
    
    form = ClientForm(instance=client)
    
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client')
        else:
            return form.errors
    
    context = {'ingroups':ingroups, "form":form, 'client':client}
    
    return render(request, "apps/client/create_client.html", context)

@login_required(login_url="login")
def client_details(request, id):
    ingroups = request.user.groups.exists()
    client = Client.objects.get(id=id)
    
    context = {'ingroups':ingroups, "client":client}
    
    return render(request, "apps/client/client_details.html", context)

@login_required(login_url="login")
def delete_client(request, id):
    ingroups = request.user.groups.exists()
    client = Client.objects.get(id=id)
    client.delete()
    messages.success(request, "Le client supprimé avec succès!")
    
    context = {'ingroups':ingroups, 'client':client}
    
    return redirect('client')