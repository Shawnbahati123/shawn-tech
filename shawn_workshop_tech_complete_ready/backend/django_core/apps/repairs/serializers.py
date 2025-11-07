from rest_framework import serializers
from .models import ServiceTicket, TicketPart

class TicketPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketPart
        fields = '__all__'

class ServiceTicketSerializer(serializers.ModelSerializer):
    parts = TicketPartSerializer(many=True, required=False)

    class Meta:
        model = ServiceTicket
        fields = '__all__' 