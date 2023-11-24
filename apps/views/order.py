from django.shortcuts import redirect, render

def order(request):
    context = {}
    return render(request, "apps/order/order.html", context)