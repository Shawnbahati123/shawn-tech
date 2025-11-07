from rest_framework.viewsets import ModelViewSet
from .models import ServiceTicket
from .serializers import ServiceTicketSerializer

class ServiceTicketViewSet(ModelViewSet):
    queryset = ServiceTicket.objects.all()
    serializer_class = ServiceTicketSerializer