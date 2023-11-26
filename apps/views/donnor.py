from django.shortcuts import redirect, render

def donnor(request):
    context = {}
    return render(request, "apps/donnor/donnor.html", context)