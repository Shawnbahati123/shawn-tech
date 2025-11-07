from rest_framework.viewsets import ModelViewSet
from .models import NotificationTemplate
from rest_framework import serializers

class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = '__all__'

class NotificationTemplateViewSet(ModelViewSet):
    queryset = NotificationTemplate.objects.all()
    serializer_class = NotificationTemplateSerializer