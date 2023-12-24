from django.shortcuts import render, redirect


def public(request):
    context = {}
    return render(request, "apps/public/index.html", context)