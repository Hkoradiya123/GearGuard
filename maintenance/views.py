from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MaintenanceRecord
from equipment.models import Equipment


@login_required
def maintenance_list(request):
    records = (
        MaintenanceRecord.objects
        .select_related('equipment', 'equipment__category')
        .order_by('-service_date')
    )
    equipment_list = Equipment.objects.filter(status='active').order_by('name')
    return render(request, 'maintenance/list.html', {
        'records': records,
        'equipment_list': equipment_list
    })
