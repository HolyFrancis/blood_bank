from django.shortcuts import redirect, render

def home(request):
    context = {}
    return render(request, "apps/home/index.html", context)