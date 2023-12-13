from django.shortcuts import redirect, render
from django.contrib import messages

from apps.models import Analysis
from apps.forms import AnalysisForm

def analyse(request):
    analyses = Analysis.objects.all()
    
    context = {'analyses':analyses}
    
    return render(request, "apps/analyse/analyse.html", context)

def create_analysis(request):
    form = AnalysisForm()
    
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analyse')
    
    context = {"form":form}
    
    return render(request, "apps/analyse/create_analyse.html", context)

def update_analysis(request, id):
    analysis = Analysis.objects.get(id=id)
    
    form = AnalysisForm(instance=analysis)
    
    if request.method == "POST":
        form = AnalysisForm(request.POST, instance=analysis)
        if form.is_valid():
            form.save()
            return redirect('analyse')
        else:
            return form.errors
    
    context = {"form":form, 'analysis':analysis}
    
    return render(request, "apps/donor/create_donor.html", context)

def delete_analysis(request, id):
    analysis = Analysis.objects.get(id=id)
    analysis.delete()
    messages.success(request, "Donor deleted successefuly!")
    
    context = {'analysis':analysis}
    
    return redirect('analyse')