from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from apps.models import Solution
from apps.forms import SolutionForm

@login_required(login_url="login")
def solution(request):
    ingroups = request.user.groups.exists()
    products = Solution.objects.all()
    solutions = Solution.objects.all()
    context = {'ingroups':ingroups, "solutions": solutions}

    return render(request, "apps/solution/solution.html", context)

@login_required(login_url="login")
def save_solution(request):
    ingroups = request.user.groups.exists()
    create = True
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

    context = {'ingroups':ingroups, "form": form, "create":create}
    return render(request, "apps/solution/create_solution.html", context)

@login_required(login_url="login")
def update_solution(request, id):
    ingroups = request.user.groups.exists()
    create = False
    product_type = Solution.objects.get(id=id)
    form = SolutionForm(instance=product_type)

    if request.method == "POST":
        form = SolutionForm(request.POST, instance=product_type)
        if form.is_valid():
            form.save()
            item = request.POST
            messages.success(request, item['name'] + " modifié avec succès")
        return redirect("solution")

    context = {'ingroups':ingroups, "form": form, "solution": product_type, "create":create}

    return render(request, "apps/solution/create_solution.html", context)

@login_required(login_url="login")
def delete_solution(request, id):
    ingroups = request.user.groups.exists()
    solution = Solution.objects.get(id=id)
    solution.delete()
    messages.success(request, "Solution supprimé avec succès")

    return redirect("solution")