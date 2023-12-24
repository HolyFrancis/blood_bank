from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from apps.forms import UserForm, PasswordChangingForm, GroupForm
from apps.decorators import gohome_if_authenticated

User = get_user_model()

@login_required(login_url="login")
def users(request):
    ingroups = request.user.groups.exists()
    users = User.objects.all()
    
    groupusers = []
    
    for user in users:
        if user.groups.exists() is True:
            groupusers.append(user)
    
    context = {'ingroups':ingroups, 'users':groupusers}
    
    return render(request, "apps/user/users.html", context)

@login_required(login_url="login")
def settings(request):
    ingroups = request.user.groups.exists()
    
    context={'ingroups':ingroups}
    
    return render(request, "apps/user/settings.html", context)

@gohome_if_authenticated
def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST["username"]
        if request.POST["password"] != request.POST["password_confirm"]:
            messages.error(request, "Les mots de passes saisis ne sont pas identiques")
            return render(request, "apps/user/register.html")
        elif User.objects.filter(username=username).exists():
            messages.error(
                request,
                "Un utilisateur avec le nom de "
                + username
                + " existe déjà. Veuillez saisir un autre nom d'utilisateur",
            )
            return render(request, "apps/user/register.html")
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "L'utilisateur " + username + " a été créé avec succès")
            return redirect("login")
    return render(request, "apps/user/register.html", {"form": form})

@gohome_if_authenticated
def loginview(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "apps/user/login.html")

@login_required(login_url="login")
def user_requests(request):
    ingroups = request.user.groups.exists()
    users = User.objects.all()
    nogroupusers = []
    
    for user in users:
        if user.groups.exists() is False:
            nogroupusers.append(user)
            
    form = GroupForm()
    
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            user_id = request.GET.get('user_id')
            user = User.objects.get(id=user_id)
            user.groups.add(Group.objects.get(name=form.cleaned_data['groups']))
            user.save()
            return redirect("user_requests")
        
    context = {'ingroups':ingroups, 'users':nogroupusers, 'form':form}
    
    return render(request, "apps/user/requests.html", context)

def logoutview(request):
    logout(request)
    return redirect("login")

class changePassword(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    messages.success(request, "Le mot de passe a été changé avec succès")
    return render(request, "apps/user/settings.html")