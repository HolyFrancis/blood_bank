from django.shortcuts import redirect, render

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