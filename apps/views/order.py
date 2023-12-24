from django.shortcuts import redirect, render
from django.contrib import messages
from django.forms import formset_factory

from apps.models import Order, Type_PSL, PSL
from apps.forms import OrderForm, SerialForm

from apps.views.home import counts

def order(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "apps/order/order.html", context)


def create_order(request):
    of = request.GET.get("of")

    if of == "gr":
        type_psl = Type_PSL.objects.get(name="GR")
    elif of == "pfc":
        type_psl = Type_PSL.objects.get(name="PFC")
    elif of == "cps":
        type_psl = Type_PSL.objects.get(name="CPS")
        
    psls = PSL.objects.filter(type_psl=type_psl, dispo=True)
    psls_bags_count = counts(psls)
        
    form = OrderForm(initial={"type_psl": type_psl})
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            
            if order.quantity_A_plus > psls_bags_count['A+'] or order.quantity_A_m > psls_bags_count['A-'] or order.quantity_B_plus > psls_bags_count['B+'] or order.quantity_B_m > psls_bags_count['B-'] or order.quantity_AB_plus > psls_bags_count['AB+'] or order.quantity_AB_m > psls_bags_count['AB-'] or order.quantity_O_plus > psls_bags_count['O+'] or order.quantity_O_m > psls_bags_count['O-']:
               
                messages.error(request, "Vous ne pouvez pas commander une quantité supérieure à la quantité disponible")
                context = {"form": form, 'type_psl':type_psl.name, 'psls_bags_count':psls_bags_count.items()}
                return render(request, "apps/order/create_order.html", context)
            
            order.save()
            messages.success(request, "Commande N°" + str(order.id) + " ajoutée avec succès!")
            return redirect("order")
    context = {"form": form, 'type_psl':type_psl.name, 'psls_bags_count':psls_bags_count.items()}
    return render(request, "apps/order/create_order.html", context)


def update_order(request, id):
    order = Order.objects.get(id=id)

    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            messages.success(request, "Commande N°" + str(order.id) + " modifiée avec succès!")
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
        messages.success(request, "La commande N°" + str(id) + " a été approuvée et attend d'être délivrée au client ")
    elif q == "reject":
        blood_order.status = "Annulée"
        blood_order.save()
        messages.warning(request, "Commande N°" + str(id) + " rejetée")

    return redirect("order_requests")


def blood_order_history(request):
    blood_order = Order.objects.filter(status="Confirmée")
    dorders = Order.objects.filter(status="Délivrée")
    context = {"orders": blood_order, 'dorders':dorders}

    return render(request, "apps/order/order_history.html", context)


def blood_history_decision(request, id):
    blood_order = Order.objects.get(id=id)
    dispo_psls = PSL.objects.filter(dispo=True)

    SerialFormSet = formset_factory(SerialForm, extra=blood_order.get_total_quantity)
    formset = SerialFormSet()
    print('Before post')
    
    if request.method == "POST":
        formset = SerialFormSet(request.POST)
        
        if formset.is_valid():
            for form in formset:
                exsts = False
                for dispo_psl in dispo_psls:
                    if form.cleaned_data['serial'] == dispo_psl.serial:
                         exsts = True
                         break
                if exsts == False:
                    messages.error(request, "Un ou pulsieurs numéros de série sont incorrect")
                    
                    context = {'formset': formset, 'q':blood_order.get_total_quantity, 'psls':dispo_psls}
            
                    return render(request, "apps/order/submit_psls.html", context)
                
            for form in formset:
                psl = PSL.objects.get(serial=form.cleaned_data["serial"])
                psl.dispo = False
                psl.save()
                
            blood_order.status = "Délivrée"
            blood_order.save()
            messages.success(request, "la commande de " + blood_order.client.name + " a été delivrée")
            return redirect('order_history')
    
        else:
            print(formset.errors)

    context = {'formset': formset, 'q':blood_order.get_total_quantity, 'psls':dispo_psls}
    
    return render(request, "apps/order/submit_psls.html", context)