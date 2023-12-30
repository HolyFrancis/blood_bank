from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from apps.models import Analysis, Blood
from apps.forms import AnalysisForm
from apps.filters import AnalysisFilter

from apps.decorators import allowed_users, disallowed_users


@login_required(login_url="login")
@disallowed_users(['Client'])
def analyse(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    
    analyses = Analysis.objects.all()
    filtre = AnalysisFilter(request.GET, queryset=analyses)
    analyses = filtre.qs
    
    context = {'ingroups':ingroups, 'analyses':analyses, "filtre":filtre}
    
    return render(request, "apps/analyse/analyse.html", context)

@login_required(login_url="login")
@allowed_users(['Laborantin'])
def create_analysis(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    
    blood = Blood.objects.get(id=id)
    form = AnalysisForm(initial={'blood':blood})
    
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)
            
            if analysis.irregular_antibodies == 'Négatif' and analysis.hiv_test == 'Négatif' and analysis.hepatites_test == 'Négatif' and analysis.anti_hlv1_test == 'Négatif' and analysis.anti_hlv2_test == 'Négatif' and analysis.malaria_test == 'Négatif':
                analysis.result = 'Négatif'
            else:
                analysis.result = 'Positif'
                
            analysis.save()
            
            if analysis.result=='Négatif':
                blood.state = 'Eligible'
            elif analysis.result=="Positif":
                blood.state = 'Ineligible'
                
            blood.analysed = True
            blood.save()
            item = request.POST
            messages.success(request, "Analyse pour la " + str(blood) + " créée avec succès")
            return redirect('request_analysis')
        else:
            print(form.errors)
    
    context = {'ingroups':ingroups, "form":form, "blood":blood}
    
    return render(request, "apps/analyse/create_analyse.html", context)

@login_required(login_url="login")
@allowed_users(['Laborantin'])
def update_analysis(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    
    analysis = Analysis.objects.get(id=id)
    blood = Blood.objects.get(id=analysis.blood)
    
    form = AnalysisForm(instance=analysis)
    
    if request.method == "POST":
        form = AnalysisForm(request.POST, instance=analysis)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, "Analyse pour la " + str(blood) + " modifiée avec succès")
            return redirect('analyse')
        else:
            return form.errors
    
    context = {'ingroups':ingroups, "form":form, 'analysis':analysis}
    
    return render(request, "apps/analyse/create_analyse.html", context)

@login_required(login_url="login")
@disallowed_users(['Client'])
def analysis_details(request, id):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    
    analysis = Analysis.objects.get(id=id)
    
    context = {'ingroups':ingroups, 'analysis':analysis}
    
    return render(request, "apps/analyse/details.html", context)

@login_required(login_url="login")
@allowed_users(["Laborantin"])
def delete_analysis(request, id):    
    
    analysis = Analysis.objects.get(id=id)
    analysis.delete()
    messages.success(request, "Analyse supprimée avec succès")
    
    return redirect('analyse')

@login_required(login_url="login")
@allowed_users(['Laborantin'])
def request_analysis(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    bloods = Blood.objects.filter(analysed=False)
    
    context = {'ingroups':ingroups, 'bloods':bloods}
    
    return render(request, "apps/analyse/requests.html", context)

@login_required(login_url="login")
@allowed_users(['Laborantin'])
def analysis_history(request):
    role = request.user.role    
    if role is None:
        ingroups = False
    else:
        ingroups = True
     
    analyses = Analysis.objects.all()
    
    context = {'ingroups':ingroups, 'analyses':analyses}
    
    return render(request, "apps/analyse/history.html", context)