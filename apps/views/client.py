from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.models import Client, Users
from apps.forms.client import ClientForm
from apps.decorators import allowed_users

@login_required(login_url="login")
def client(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    clients = Client.objects.all()
    context = {'ingroups':ingroups, "clients":clients}
    return render(request, "apps/client/client.html", context)

@login_required(login_url="login")
def create_client(request):
    role = request.user.role    
    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = Users.objects.create_user(form.cleaned_data['name'], password=form.cleaned_data["password"])
            client.user.first_name = form.cleaned_data['name']
            client.user.email = form.cleaned_data['email']
            client.user.role = 'Client'
            client.user.phone_number = form.cleaned_data["phone"]
            client.user.save()
            client.save()
            return redirect('client')
        else:
            print(form.errors)
    context = {'ingroups':ingroups, "form":form}
    return render(request, "apps/client/create_client.html", context)

@login_required(login_url="login")
def update_client(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
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
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    client = Client.objects.get(id=id)
    
    context = {'ingroups':ingroups, "client":client}
    
    return render(request, "apps/client/client_details.html", context)

@login_required(login_url="login")
def delete_client(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    client = Client.objects.get(id=id)
    client.delete()
    messages.success(request, "Le client supprimé avec succès!")
    
    context = {'ingroups':ingroups, 'client':client}
    
    return redirect('client')