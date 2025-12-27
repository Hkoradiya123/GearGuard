from django.db import models


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=100)
    responsible = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name


class Equipment(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
    ]

    asset_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=120)
    category = models.ForeignKey(EquipmentCategory, on_delete=models.SET_NULL, null=True, related_name="equipments")
    company = models.CharField(max_length=100, blank=True)
    serial_no = models.CharField(max_length=100, blank=True)
    technician = models.CharField(max_length=100, blank=True)
    maintenance_team = models.CharField(max_length=100, blank=True)
    assigned_date = models.DateField(null=True, blank=True)
    maintenance_interval_days = models.PositiveIntegerField(default=90)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.asset_id} - {self.name}"
