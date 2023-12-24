from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from apps.models import Donor, Blood, PSL, Type_PSL

def counts(modelObject):
    a_plus_bags = 0
    b_plus_bags = 0
    ab_plus_bags = 0
    o_plus_bags = 0
    a_minus_bags = 0
    b_minus_bags = 0
    ab_minus_bags = 0
    o_minus_bags = 0
    
    for psl in modelObject:
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
        
    return bags_counts

@login_required(login_url="public")
def home(request):
    ingroups = request.user.groups.exists()
    
    if ingroups:
    
        #--------------------------------------Donors Stats----------------------------------------

        donors_count = Donor.objects.all().count()
        eligible_donors = Donor.objects.filter(status = 'Eligible').count()
        ineligible_donors = Donor.objects.filter(status='Ineligible').count()
        pending_donors = Donor.objects.filter(status='Attente').count()

        eligible_donors_percent = 0
        ineligible_donors_percent = 0
        pending_donors_percent = 0
        if donors_count is not 0:
            eligible_donors_percent = eligible_donors/donors_count*100
            ineligible_donors_percent = ineligible_donors/donors_count*100
            pending_donors_percent = pending_donors/donors_count*100
            
            
        #--------------------------------------Bloods Stats----------------------------------------
        not_yet_centrifuged_bloods = Blood.objects.filter(centrifuged=False)
        bloods_count = not_yet_centrifuged_bloods.count()
        eligible_bloods = not_yet_centrifuged_bloods.filter(state='Eligible').count()
        ineligible_bloods = not_yet_centrifuged_bloods.filter(state='Ineligible').count()
        pending_bloods = not_yet_centrifuged_bloods.filter(state='Attente').count()

        eligible_bloods_percent = 0
        ineligible_bloods_percent = 0
        pending_bloods_percent = 0
        if eligible_bloods is not 0:
            eligible_bloods_percent = eligible_bloods/bloods_count*100
            ineligible_bloods_percent = ineligible_bloods/bloods_count*100
            pending_bloods_percent = pending_bloods/bloods_count*100
            

        #--------------------------------------PSLs Stats----------------------------------------
        try:
            gr = Type_PSL.objects.get(name='GR')
            cps = Type_PSL.objects.get(name='CPS')
            pfc = Type_PSL.objects.get(name='PFC')
        except Type_PSL.DoesNotExist:
            gr = None
            cps = None
            pfc = None
            
        gr_count = PSL.objects.filter(type_psl=gr, dispo=True).count()
        cps_count = PSL.objects.filter(type_psl=cps, dispo=True).count()
        pfc_count = PSL.objects.filter(type_psl=pfc,dispo=True).count()
        
        indispo_gr_count = PSL.objects.filter(type_psl=gr, dispo=False).count()
        indispo_cps_count = PSL.objects.filter(type_psl=cps, dispo=False).count()
        indispo_pfc_count = PSL.objects.filter(type_psl=pfc, dispo=False).count()
        
        psls = PSL.objects.all()
        psls_gr = PSL.objects.filter(type_psl=gr)
        psls_pfc = PSL.objects.filter(type_psl=pfc)
        psls_cps = PSL.objects.filter(type_psl=cps)
        
        psls_bags_count = counts(psls)
        gr_bags_count = counts(psls_gr)
        pfc_bags_count = counts(psls_pfc)
        cps_bags_count = counts(psls_cps)

        #-------------------------------------------End Stats---------------------------------------
            
        context = {
            'donors_count':donors_count,
            'eligible_donors':eligible_donors,
            'ineligible_donors':ineligible_donors,
            'pending_donors':pending_donors,
            'eligible_donors_percent':eligible_donors_percent, 
            'ineligible_donors_percent':ineligible_donors_percent,
            'pending_donors_percent':pending_donors_percent,
            
            'bloods_count':bloods_count,
            'eligible_bloods':eligible_bloods,
            'ineligible_bloods':ineligible_bloods,
            'pending_bloods':pending_bloods, 
            'eligible_bloods_percent':eligible_bloods_percent,
            'ineligible_bloods_percent':ineligible_bloods_percent,
            'pending_bloods_percent':pending_bloods_percent,
            
            'gr_count':gr_count, 
            'cps_count':cps_count,
            'pfc_count':pfc_count,
            
            'indispo_gr_count':indispo_gr_count, 
            'indispo_cps_count':indispo_cps_count,
            'indispo_pfc_count':indispo_pfc_count,
            
            'psls_bags_count':psls_bags_count.items(),
            'gr_bags_count':gr_bags_count.items(),
            'pfc_bags_count':pfc_bags_count.items(),
            'cps_bags_count':cps_bags_count.items(),
            
            'ingroups':ingroups
            }
    else:
        context = {'ingroups':ingroups}
    
    return render(request, "apps/home/index.html", context)