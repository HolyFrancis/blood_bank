from django.shortcuts import redirect, render

def psl(request):
    context = {}
    return render(request, "apps/psl/psl.html", context)