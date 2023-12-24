from django.shortcuts import redirect, render
from django.contrib import messages

from apps.models import Analysis, Blood
from apps.forms import AnalysisForm
from apps.filters import AnalysisFilter


def analyse(request):
    analyses = Analysis.objects.all()
    filtre = AnalysisFilter(request.GET, queryset=analyses)
    analyses = filtre.qs

    context = {"analyses": analyses, "filtre": filtre}

    return render(request, "apps/analyse/analyse.html", context)


def create_analysis(request, id):
    blood = Blood.objects.get(id=id)
    form = AnalysisForm(initial={"blood": blood})

    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)

            if (
                analysis.irregular_antibodies == "Négatif"
                and analysis.hiv_test == "Négatif"
                and analysis.hepatites_test == "Négatif"
                and analysis.anti_hlv1_test == "Négatif"
                and analysis.anti_hlv2_test == "Négatif"
                and analysis.malaria_test == "Négatif"
            ):
                analysis.result = "Négatif"
            else:
                analysis.result = "Positif"

            analysis.save()

            if analysis.result == "Négatif":
                blood.state = "Eligible"
            elif analysis.result == "Positif":
                blood.state = "Ineligible"

            blood.analysed = True
            blood.save()
            # item = request.POST
            messages.success(request, "Analyse pour la " + str(blood) + " créée avec succès")
            return redirect("request_analysis")
        else:
            print(form.errors)

    context = {"form": form, "blood": blood}

    return render(request, "apps/analyse/create_analyse.html", context)


def update_analysis(request, id):
    analysis = Analysis.objects.get(id=id)
    blood = Blood.objects.get(id=analysis.blood.id)

    form = AnalysisForm(instance=analysis)

    if request.method == "POST":
        form = AnalysisForm(request.POST, instance=analysis)
        if form.is_valid():
            form.save()
            # item = request.POST
            messages.success(request, "Analyse pour la " + str(blood) + " modifiée avec succès")
            return redirect("analyse")
        else:
            return form.errors

    context = {"form": form, "analysis": analysis}

    return render(request, "apps/analyse/create_analyse.html", context)


def analysis_details(request, id):
    analysis = Analysis.objects.get(id=id)

    context = {"analysis": analysis}

    return render(request, "apps/analyse/details.html", context)


def delete_analysis(request, id):
    analysis = Analysis.objects.get(id=id)
    analysis.delete()
    messages.success(request, "Analyse supprimée avec succès")

    return redirect("analyse")


def request_analysis(request):
    bloods = Blood.objects.filter(analysed=False)

    context = {"bloods": bloods}

    return render(request, "apps/analyse/requests.html", context)


def analysis_history(request):
    analyses = Analysis.objects.all()

    context = {"analyses": analyses}

    return render(request, "apps/analyse/history.html", context)
