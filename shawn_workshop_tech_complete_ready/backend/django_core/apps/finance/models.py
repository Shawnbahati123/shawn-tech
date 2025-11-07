from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class FinanceSnapshot(models.Model):
    period_start = models.DateField()
    period_end = models.DateField()
    revenue = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    cogs = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    gross_profit = models.DecimalField(max_digits=14, decimal_places=2, default=0)