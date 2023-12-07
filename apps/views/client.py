from django.shortcuts import redirect, render

def client(request):
    context = {}
    return render(request, "apps/client/client.html", context)