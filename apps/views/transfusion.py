from django.shortcuts import redirect, render

def transfusion(request):
    context = {}
    return render(request, "apps/transfusion/transfusion.html", context)