from django.contrib import admin
from .models import EquipmentCategory, Equipment

@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "responsible", "company")
    search_fields = ("name", "responsible", "company")

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("asset_id", "name", "category", "status", "assigned_date")
    list_filter = ("status", "category")
    search_fields = ("asset_id", "name", "serial_no")
