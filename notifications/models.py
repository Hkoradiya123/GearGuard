from django.db import models


class Notification(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("read", "Read"),
        ("dismissed", "Dismissed"),
    ]

    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_date = models.DateTimeField(auto_now_add=True)
    equipment = models.ForeignKey('equipment.Equipment', on_delete=models.SET_NULL, null=True, blank=True, related_name='notifications')

    def __str__(self) -> str:
        return f"{self.get_status_display()} - {self.message[:40]}"
