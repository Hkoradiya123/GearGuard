from django.contrib import admin
from .models import MaintenanceRecord

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ("equipment", "service_date", "next_due", "status", "technician", "cost")
    list_filter = ("status", "service_date")
    search_fields = ("equipment__name", "equipment__asset_id", "technician")
