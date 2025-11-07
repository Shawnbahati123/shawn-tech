from django.db import models

class NotificationTemplate(models.Model):
    name = models.CharField(max_length=200)
    channel = models.CharField(max_length=50, default='sms')
    template = models.TextField()

    def __str__(self):
        return self.name