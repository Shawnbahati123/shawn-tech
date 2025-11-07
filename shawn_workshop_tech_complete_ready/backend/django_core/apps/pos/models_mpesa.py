from django.db import models
from django.utils import timezone

class MPesaTransaction(models.Model):
    mpesa_receipt = models.CharField(max_length=200, blank=True, null=True)
    invoice_no = models.CharField(max_length=200, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')  # pending, paid, failed
    raw_payload = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_paid(self):
        self.status = 'paid'
        self.save()
