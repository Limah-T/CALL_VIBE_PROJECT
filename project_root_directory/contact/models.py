from django.db import models
from django.conf import settings
# Create your models here.

class Contact(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contacts")
    contact_number = models.CharField(max_length=15, null=False, blank=False)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
