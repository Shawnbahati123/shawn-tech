from django.db import models
from apps.inventory.models import Product

class Sale(models.Model):
    invoice_no = models.CharField(max_length=100, unique=True)
    cashier = models.ForeignKey('apps.users.User', on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)