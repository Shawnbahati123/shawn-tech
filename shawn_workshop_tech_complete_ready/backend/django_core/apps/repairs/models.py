from django.db import models

class ServiceTicket(models.Model):
    ticket_no = models.CharField(max_length=120, unique=True)
    customer_name = models.CharField(max_length=200)
    device_info = models.CharField(max_length=255)
    problem_description = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='received')
    assigned_to = models.ForeignKey('apps.users.User', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

class TicketPart(models.Model):
    ticket = models.ForeignKey(ServiceTicket, related_name='parts', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    qty = models.IntegerField()