from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from apps.forms.user import UserForm, PasswordChangingForm

User = get_user_model()

def users(request):
    context = {}
    
    return render(request, "apps/user/users.html", context)

def settings(request):
    
    context={}
    
    return render(request, "apps/user/settings.html", context)

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
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "L'utilisateur " + username + " a été créé avec succè")
            return redirect("login")
    return render(request, "apps/user/register.html", {"forms": form})


def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")
    return render(request, "apps/user/login.html")


def logoutview(request):
    logout(request)
    return redirect("login")

class changePassword(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    messages.success(request, "Le mot de passe a été changé avec succès")
    return render(request, "apps/user/settings.html")