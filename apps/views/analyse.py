from django.shortcuts import redirect, render

def analyse(request):
    context = {}
    return render(request, "apps/analyse/analyse.html", context)