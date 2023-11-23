from django.shortcuts import redirect, render

def hressource(request):
    context = {}
    return render(request, "apps/hressource/hressource.html", context)