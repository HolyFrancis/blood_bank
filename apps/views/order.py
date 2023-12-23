from django.shortcuts import redirect, render
from apps.models import Order, Type_PSL
from django.contrib import messages
from apps.forms import OrderForm


def order(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "apps/order/order.html", context)


def create_order(request):
    # types_psl = Type_PSL.objects.get(id=id)
    of = request.GET.get("of")

    if of == "gr":
        type_psl = Type_PSL.objects.get(name="GR")
    elif of == "pfc":
        type_psl = Type_PSL.objects.get(name="PFC")
    elif of == "cps":
        type_psl = Type_PSL.objects.get(name="CPS")
    form = OrderForm(initial={"type_psl": type_psl})
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order")
    context = {"form": form}
    return render(request, "apps/order/create_order.html", context)


def update_order(request, id):
    order = Order.objects.get(id=id)

    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            # item = request.POST
            return redirect("order")

    context = {"form": form, "order": order}

    return render(request, "apps/order/create_order.html", context)


def delete_order(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    messages.success(request, "La commande a été supprimé avec succès!")

    return redirect("order")


#
