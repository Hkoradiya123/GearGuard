from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Equipment, EquipmentCategory


@login_required
def equipment_list(request):
    items = Equipment.objects.select_related('category').all().order_by('asset_id')
    categories = EquipmentCategory.objects.all()
    return render(request, 'equipment/list.html', {
        'items': items,
        'categories': categories
    })


@login_required
def equipment_detail(request, pk: int):
    item = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipment/detail.html', {'item': item})


@login_required
def add_equipment(request):
    if request.method == 'POST':
        # Get or create category
        category_name = request.POST.get('category_name', 'General')
        category, created = EquipmentCategory.objects.get_or_create(
            name=category_name,
            defaults={'responsible': 'Admin', 'company': 'Default Company'}
        )
        
        # Create equipment
        equipment = Equipment.objects.create(
            asset_id=request.POST.get('asset_id'),
            name=request.POST.get('name'),
            category=category,
            company=request.POST.get('company', ''),
            serial_no=request.POST.get('serial_no', ''),
            technician=request.POST.get('technician', ''),
            maintenance_team=request.POST.get('maintenance_team', ''),
            maintenance_interval_days=int(request.POST.get('maintenance_interval_days', 90)),
            status=request.POST.get('status', 'active'),
            description=request.POST.get('description', '')
        )
        
        messages.success(request, f'Equipment "{equipment.asset_id}" added successfully!')
        return redirect('equipment_list')
    
    categories = EquipmentCategory.objects.all()
    return render(request, 'equipment/add.html', {'categories': categories})
