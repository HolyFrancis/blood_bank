from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from apps.forms import UserForm, PasswordChangingForm, RoleForm
from apps.models import Users
from apps.decorators import gohome_if_authenticated

User = get_user_model()

@login_required(login_url="login")
def users(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    users = User.objects.all()
    
    roleusers = []
    
    for user in users:
        if user.role is not None:
            roleusers.append(user)
    
    context = {'ingroups':ingroups, 'users':roleusers}
    
    return render(request, "apps/user/users.html", context)

@login_required(login_url="login")
def settings(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
    
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
            return render(request, "apps/user/register.html", {'form', form})
        elif User.objects.filter(username=username).exists():
            messages.error(
                request,
                "Un utilisateur avec le nom de "
                + username
                + " existe déjà. Veuillez saisir un autre nom d'utilisateur",
            )
            return render(request, "apps/user/register.html", {'form', form})
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
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    users = User.objects.all()
    noroleusers = []
    
    for user in users:
        if user.role is None:
            noroleusers.append(user)
            
    form = RoleForm()
    
    if request.method == "POST":
        form = RoleForm(request.POST)
        if form.is_valid():
            user_id = request.GET.get('user_id')
            user = User.objects.get(id=user_id)
            user.role = form.cleaned_data['role']
            user.save()
            
            return redirect("user_requests")
        
    context = {'ingroups':ingroups, 'users':noroleusers, 'form':form}
    
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

def delete_user(request, id):
    user = Users.objects.get(id=id)
    user.is_active = False
    redirect('users')