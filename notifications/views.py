from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required
def notification_list(request):
    items = Notification.objects.select_related('equipment').order_by('-created_date')
    return render(request, 'notifications/list.html', {'items': items})
