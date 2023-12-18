from django.shortcuts import redirect, render
from django.contrib import messages

from apps.models import Analysis, Blood_analysis
from apps.forms import AnalysisForm, BloodAnalysisForm


def analyse(request):
    analyses = Blood_analysis.objects.all()
    typ_analyses = Analysis.objects.all()
    
    context = {'analyses':analyses, 'typ_analyses':typ_analyses}
    
    return render(request, "apps/analyse/analyse.html", context)


def create_type_analysis(request):
    form = AnalysisForm()
    
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['typ'] + " créé avec succès")
            return redirect('analyse')
    
    context = {"form":form}
    
    return render(request, "apps/analyse/create_type.html", context)

def update_type_analysis(request, id):
    typ_analysis = Analysis.objects.get(id=id)
    
    form = AnalysisForm(instance=typ_analysis)
    
    if request.method == "POST":
        form = AnalysisForm(request.POST, instance=typ_analysis)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['typ'] + " modifié avec succès")
            return redirect('analyse')
        else:
            return form.errors
    
    context = {"form":form, 'typ_analysis':typ_analysis}
    
    return render(request, "apps/analyse/create_type.html", context)


def type_analysis_details(request, id):
    typ_analysis = Analysis.objects.get(id=id)
    
    reactants = typ_analysis.reactant.all()
    
    context = {'reactants':reactants}
    
    return render(request, "apps/analyse/type_details.html", context)


def delete_type_analysis(request, id):
    typ_analysis = Analysis.objects.get(id=id)
    typ_analysis.delete()
    messages.success(request, "Type d'analyse supprimé avec succès")
    
    context = {'typ_analysis':typ_analysis}
    
    return redirect('analyse')


def create_analysis(request):
    form = BloodAnalysisForm()
    
    if request.method == "POST":
        form = BloodAnalysisForm(request.POST)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, "Analyse : " + item['analysis'] + " pour " + item['blood'] + " créé avec succès")
            return redirect('analyse')
        else:
            print(form.errors)
    
    context = {"form":form}
    
    return render(request, "apps/analyse/create_analyse.html", context)

def update_analysis(request, id):
    analysis = Blood_analysis.objects.get(id=id)
    
    form = BloodAnalysisForm(instance=analysis)
    
    if request.method == "POST":
        form = BloodAnalysisForm(request.POST, instance=analysis)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, "Analyse : " + item['analysis'] + " pour " + item['blood'] + " modifié avec succès")
            return redirect('analyse')
        else:
            return form.errors
    
    context = {"form":form, 'analysis':analysis}
    
    return render(request, "apps/analyse/create_analyse.html", context)

def delete_analysis(request, id):
    analysis = Blood_analysis.objects.get(id=id)
    analysis.delete()
    messages.success(request, "Analyse supprimée avec succès")
    
    context = {'analysis':analysis}
    
    return redirect('analyse')