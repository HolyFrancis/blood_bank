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


def BloodQantityOrderDetatils(request, id):
    blood_order = Order.objects.get(id=id)

    context = {"order": blood_order}
    return render(request, "apps/order/quantity_details.html", context)


def order_request(request):
    orders = Order.objects.filter(status="En Attente")
    context = {"orders": orders}

    return render(request, "apps/order/order_requests.html", context)


def blood_order_decision(request, id):
    blood_order = Order.objects.get(id=id)

    q = request.GET.get("q")

    if q == "confirm":
        blood_order.status = "Confirmée"
        blood_order.save()
        messages.success(request, "la commande  a été approuvée et attend d'être délivrée au client ")
    elif q == "reject":
        blood_order.status = "Annulée"
        blood_order.save()
        messages.warning(request, "la commande du client est rejetée ")

    return redirect("order_requests")


def blood_order_history(request):
    blood_order = Order.objects.filter(status="Confirmée")
    context = {"orders": blood_order}

    return render(request, "apps/order/order_history.html", context)


def blood_history_decision(request, id):
    blood_order = Order.objects.get(id=id)

    q = request.GET.get("q")
    if q == "delivered":
        blood_order.status = "Délivrée"
        blood_order.save()
        messages.success(request, "la commande de " + blood_order.client.name + " a été delivrée")

    return redirect("order_history")
