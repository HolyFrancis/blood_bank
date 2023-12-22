from django.shortcuts import redirect, render

from apps.models import Donor, Blood, PSL, Type_PSL

def home(request):
    donors_count = Donor.objects.all().count()
    eligible_donors = Donor.objects.filter(status = 'Eligible').count()
    ineligible_donors = Donor.objects.filter(status='Ineligible').count()
    pending_donors = Donor.objects.filter(status='Attente').count()
    
    bloods_count = Blood.objects.all().count()
    eligible_bloods = Blood.objects.filter(state='Eligible').count()
    ineligible_bloods = Blood.objects.filter(state='Ineligible').count()
    pending_bloods = Blood.objects.filter(state='Attente').count()
    
    gr = Type_PSL.objects.get(name='GR')
    cps = Type_PSL.objects.get(name='CPS')
    pfc = Type_PSL.objects.get(name='PFC')
    gr_count = PSL.objects.filter(type_psl=gr).count()
    cps_count = PSL.objects.filter(type_psl=cps).count()
    pfc_count = PSL.objects.filter(type_psl=pfc).count()
    
    a_plus_bags = 0
    b_plus_bags = 0
    ab_plus_bags = 0
    o_plus_bags = 0
    a_minus_bags = 0
    b_minus_bags = 0
    ab_minus_bags = 0
    o_minus_bags = 0
    psls = PSL.objects.all()
    for psl in psls:
        if psl.blood.donor.blood_group == 'A+':
            a_plus_bags = a_plus_bags + 1
        elif psl.blood.donor.blood_group == 'B+':
            b_plus_bags = b_plus_bags + 1
        elif psl.blood.donor.blood_group == 'AB+':
            ab_plus_bags = ab_plus_bags + 1
        elif psl.blood.donor.blood_group == 'O+':
            o_plus_bags = o_plus_bags + 1
        elif psl.blood.donor.blood_group == 'A-':
            a_minus_bags = a_minus_bags + 1
        elif psl.blood.donor.blood_group == 'B-':
            b_minus_bags = b_minus_bags + 1
        elif psl.blood.donor.blood_group == 'AB-':
            ab_minus_bags = ab_minus_bags + 1
        elif psl.blood.donor.blood_group == 'O-':
            o_minus_bags = o_minus_bags + 1
    
    bags_counts = {
        'A+':a_plus_bags,
        'B+':b_plus_bags,
        'AB+':ab_plus_bags,
        'O+':o_plus_bags,
        'A-':a_minus_bags,
        'B-':b_minus_bags,
        'AB-':ab_minus_bags,
        'O-':o_minus_bags,
    }
    
    bags_counts_items = bags_counts.items()
    
    context = {'donors_count':donors_count,'eligible_donors':eligible_donors,'ineligible_donors':ineligible_donors, 'pending_donors':pending_donors, 'bloods_count':bloods_count, 'eligible_bloods':eligible_bloods, 'ineligible_bloods':ineligible_bloods, 'pending_bloods':pending_bloods, 'gr_count':gr_count, 'cps_count':cps_count,'pfc_count':pfc_count,'bags_counts_items':bags_counts_items}
    
    return render(request, "apps/home/index.html", context)