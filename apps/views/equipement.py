from django.shortcuts import redirect, render

def equipement(request):
    context = {}
    return render(request, "apps/equipement/equipement.html", context)