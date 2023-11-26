from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from apps.forms.user import UserForm

User = get_user_model()

def users(request):
    context = {}
    
    return render(request, "apps/user/users.html", context)

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST["username"]
        if request.POST["password"] != request.POST["password_confirm"]:
            messages.error(request, "The two passwords do not match")
            return render(request, "apps/user/register.html")
        elif User.objects.filter(username=username).exists():
            messages.error(
                request,
                "User with "
                + username
                + " username already exist please enter a different username",
            )
            return render(request, "apps/user/register.html")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "user " + username + " created succesfully")
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
            messages.error(request, "username or password incorrect")
    return render(request, "apps/user/login.html")


def logoutview(request):
    logout(request)
    return redirect("login")