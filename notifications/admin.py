from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message", "status", "created_date", "equipment")
    list_filter = ("status", "created_date")
    search_fields = ("message", "equipment__name", "equipment__asset_id")
