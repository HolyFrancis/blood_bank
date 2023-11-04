from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render

from apps.forms.user import UserForm

User = get_user_model()


def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        username = request.POST["username"]
        if request.POST["password"] != request.POST["password_confirm"]:
            messages.info(request, "the two passwords do not match")
            return render(request, "apps/register.html")
        elif User.objects.filter(username=username).exists():
            messages.info(
                request,
                "user with "
                + username
                + " username already exist please enter a different username",
            )
            return render(request, "apps/register.html")
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.info(request, "user " + username + " created succesfully")
            return redirect("login")
    return render(request, "apps/register.html", {"forms": form})


def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "username or password incorrect")
    return render(request, "apps/login.html")
