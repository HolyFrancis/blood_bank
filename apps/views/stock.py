from django.shortcuts import redirect, render

def stock(request):
    context = {}
    return render(request, "apps/stock/stock.html", context)