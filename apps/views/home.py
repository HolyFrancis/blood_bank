from django.shortcuts import redirect, render

from .statistics import donors_count, eligible_donors, ineligible_donors, pending_donors, bloods_count, eligible_bloods, ineligible_bloods, pending_bloods, gr_count, cps_count, pfc_count, psls_bags_count, gr_bags_count, pfc_bags_count, cps_bags_count, eligible_donors_percent, ineligible_donors_percent, pending_donors_percent, eligible_bloods_percent, ineligible_bloods_percent, pending_bloods_percent

def home(request):
        
    context = {'donors_count':donors_count,
               'eligible_donors':eligible_donors,
               'ineligible_donors':ineligible_donors,
               'pending_donors':pending_donors,
               'bloods_count':bloods_count,
               'eligible_bloods':eligible_bloods,
               'ineligible_bloods':ineligible_bloods,
               'pending_bloods':pending_bloods, 
               'gr_count':gr_count, 
               'cps_count':cps_count,
               'pfc_count':pfc_count,
               'psls_bags_count':psls_bags_count,
               'gr_bags_count':gr_bags_count,
               'pfc_bags_count':pfc_bags_count,
               'cps_bags_count':cps_bags_count,'eligible_donors_percent':eligible_donors_percent, 'ineligible_donors_percent':ineligible_donors_percent,'pending_donors_percent':pending_donors_percent,'eligible_bloods_percent':eligible_bloods_percent,'ineligible_bloods_percent':ineligible_bloods_percent,'pending_bloods_percent':pending_bloods_percent}
    
    return render(request, "apps/home/index.html", context)