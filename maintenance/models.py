from datetime import timedelta
from django.db import models


class MaintenanceRecord(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("overdue", "Overdue"),
    ]

    equipment = models.ForeignKey('equipment.Equipment', on_delete=models.CASCADE, related_name='maintenance_records')
    service_date = models.DateField()
    technician = models.CharField(max_length=100, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remarks = models.TextField(blank=True)
    next_due = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def save(self, *args, **kwargs):
        if not self.next_due and self.service_date and self.equipment and self.equipment.maintenance_interval_days:
            self.next_due = self.service_date + timedelta(days=self.equipment.maintenance_interval_days)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.equipment} @ {self.service_date}"
