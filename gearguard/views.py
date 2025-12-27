from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone


@login_required
def home_view(request):
    from equipment.models import Equipment
    from maintenance.models import MaintenanceRecord
    from notifications.models import Notification

    total_eq = Equipment.objects.count()
    critical_eq = Equipment.objects.filter(status='inactive').count()
    open_requests = MaintenanceRecord.objects.exclude(status='completed').count()
    overdue = MaintenanceRecord.objects.filter(status='overdue').count()
    notif_new = Notification.objects.filter(status='new').count()

    # Recent and due-soon widgets
    recent_records = (
        MaintenanceRecord.objects.select_related('equipment')
        .order_by('-service_date')[:5]
    )
    today = timezone.now().date()
    due_soon = (
        MaintenanceRecord.objects.select_related('equipment')
        .filter(status__in=['scheduled', 'overdue'], next_due__isnull=False, next_due__lte=today + timedelta(days=14))
        .order_by('next_due')[:5]
    )

    context = {
        'total_equipment': total_eq,
        'critical_equipment': critical_eq,
        'open_requests': open_requests,
        'overdue_requests': overdue,
        'new_notifications': notif_new,
        'recent_records': recent_records,
        'due_soon': due_soon,
    }
    return render(request, 'home.html', context)


def health_view(request):
    return HttpResponse('GearGuard OK')


@login_required
def calendar_view(request):
    from datetime import datetime, timedelta
    from maintenance.models import MaintenanceRecord
    import calendar
    
    # Get current date and navigate parameters
    today = datetime.now().date()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))
    
    # Get first and last day of month
    first_day = datetime(year, month, 1).date()
    last_day = datetime(year, month, calendar.monthrange(year, month)[1]).date()
    
    # Get maintenance records for this month
    records = (
        MaintenanceRecord.objects
        .filter(service_date__gte=first_day, service_date__lte=last_day)
        .select_related('equipment')
        .order_by('service_date')
    )
    
    # Group records by date
    records_by_date = {}
    for record in records:
        date_str = record.service_date.strftime('%Y-%m-%d')
        if date_str not in records_by_date:
            records_by_date[date_str] = []
        records_by_date[date_str].append(record)
    
    # Generate calendar days
    cal = calendar.monthcalendar(year, month)
    calendar_days = []
    
    for week in cal:
        week_days = []
        for day in week:
            if day == 0:
                week_days.append(None)  # Empty day (padding)
            else:
                current_date = datetime(year, month, day).date()
                date_str = current_date.strftime('%Y-%m-%d')
                week_days.append({
                    'day': day,
                    'date': current_date,
                    'records': records_by_date.get(date_str, []),
                    'is_today': current_date == today,
                    'is_past': current_date < today,
                })
        calendar_days.append(week_days)
    
    # Navigation for previous/next month
    prev_month = datetime(year, month, 1) - timedelta(days=1)
    next_month = datetime(year, month, calendar.monthrange(year, month)[1]) + timedelta(days=1)
    
    context = {
        'calendar': calendar_days,
        'current_month': datetime(year, month, 1),
        'prev_month': prev_month,
        'next_month': next_month,
        'month_name': calendar.month_name[month],
        'year': year,
    }
    
    return render(request, 'calendar.html', context)
