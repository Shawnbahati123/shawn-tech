from django.db import models

class AuditLog(models.Model):
    user = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    target_table = models.CharField(max_length=200, blank=True)
    target_id = models.CharField(max_length=200, blank=True)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']