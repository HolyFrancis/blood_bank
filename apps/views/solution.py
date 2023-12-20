from django.contrib import messages
from django.shortcuts import redirect, render

from apps.models import Solution
from apps.forms import SolutionForm

def solution(request):
    products = Solution.objects.all()
    solutions = Solution.objects.all()
    context = {"solutions": solutions}

    return render(request, "apps/solution/solution.html", context)


def save_solution(request):
    form = SolutionForm()

    if request.method == "POST":
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " ajouté avec succès")
            return redirect("solution")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "apps/solution/create_solution.html", context)


def update_solution(request, id):
    product_type = Solution.objects.get(id=id)
    form = SolutionForm(instance=product_type)

    if request.method == "POST":
        form = SolutionForm(request.POST, instance=product_type)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " modifié avec succès")
        return redirect("solution")

    context = {"form": form, "solution": product_type}

    return render(request, "apps/solution/create_solution.html", context)


def delete_solution(request, id):
    solution = Solution.objects.get(id=id)
    solution.delete()
    messages.success(request, "Solution supprimé avec succès")

    return redirect("solution")