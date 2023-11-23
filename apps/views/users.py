from django.shortcuts import redirect, render

def users(request):
    context = {}
    return render(request, "apps/users/users.html", context)