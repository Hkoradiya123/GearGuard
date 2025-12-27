from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date
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


@login_required
def add_maintenance_record(request):
    if request.method == 'POST':
        # Get equipment object
        try:
            equipment = Equipment.objects.get(id=request.POST.get('equipment'))
        except Equipment.DoesNotExist:
            messages.error(request, 'Please select a valid equipment.')
            return redirect('maintenance:list')
        
        # Create maintenance record
        service_date = parse_date(request.POST.get('service_date'))
        if not service_date:
            messages.error(request, 'Please provide a valid service date.')
            return redirect('maintenance:list')
            
        record = MaintenanceRecord.objects.create(
            equipment=equipment,
            service_date=service_date,
            status=request.POST.get('status'),
            technician=request.POST.get('technician', ''),
            cost=float(request.POST.get('cost', 0)),
            remarks=request.POST.get('notes', '')
        )
        
        messages.success(request, f'Maintenance record for "{equipment.asset_id}" added successfully!')
        return redirect('maintenance:list')
    
    equipment_list = Equipment.objects.filter(status='active').order_by('name')
    return render(request, 'maintenance/add.html', {'equipment_list': equipment_list})


@login_required
def update_maintenance_status(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')
        status = request.POST.get('status')
        
        try:
            record = MaintenanceRecord.objects.get(id=record_id)
            record.status = status
            record.save()
            
            if status == 'completed':
                messages.success(request, f'Maintenance record for "{record.equipment.asset_id}" marked as completed!')
            else:
                messages.info(request, f'Maintenance record status updated to {record.get_status_display}.')
                
        except MaintenanceRecord.DoesNotExist:
            messages.error(request, 'Maintenance record not found.')
        
        return redirect('maintenance:list')


@login_required
def maintenance_detail(request, pk):
    record = get_object_or_404(MaintenanceRecord, pk=pk)
    return render(request, 'maintenance/detail.html', {'record': record})
