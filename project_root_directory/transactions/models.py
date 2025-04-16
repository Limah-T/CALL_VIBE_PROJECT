from django.db import models
from django.utils import timezone
from django.conf import settings

STATUS = [
    ('Pending', 'Pending'),
    ('Success', 'Success'),
    ('Failed', 'Failed'),
]
class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions_wallet")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=10, default="NGN")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s wallet - {self.balance}"
    
    def funds(self, amount):
        self.balance += amount
        self.save()

    def deduct(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False

class AirtimePurchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions_airtime_purchase")
    phonenumber = models.CharField(max_length=15, null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    network = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[1])
    # Stores Africastaling API response
    provider_reference = models.CharField(max_length=100, blank=True, null=True)
    purchased_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} tried to purchase airtime of {self.amount} to {self.network} network => {self.status}"
 