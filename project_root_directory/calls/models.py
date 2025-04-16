from django.db import models
from django.conf import settings
from contact.models import Contact
from django.utils import timezone

CALL_STATUS = [
    ('completed', 'Completed'),
    ('missed', 'Missed'),
    ('failed', 'Failed'),
    ('no_answer', 'No Answer')
]

class Call(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="call")
    to_number = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name="receiver")
    from_number = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="caller")
    duration = models.PositiveIntegerField(help_text="Duration in seconds")
    call_time = models.DateTimeField(default=timezone.now)
    status =  models.CharField(max_length=15, choices=CALL_STATUS, default="completed")

    def __str__(self):
        return f"Call from {self.from_number} to {self.to_number} on {self.call_time.strftime("%Y-%m-%d %H:%M:%S")}"
