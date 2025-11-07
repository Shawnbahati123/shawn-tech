from rest_framework.viewsets import ModelViewSet
from .models import Sale, SaleItem
from .serializers import SaleSerializer
from apps.inventory.models import StockLevel, Product
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

class SaleViewSet(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        items = data.get('items', [])
        if not items:
            return Response({'detail':'items required'}, status=status.HTTP_400_BAD_REQUEST)
        with transaction.atomic():
            sale = Sale.objects.create(invoice_no=data.get('invoice_no'), cashier_id=data.get('cashier'), total=data.get('total',0))
            for it in items:
                product = Product.objects.get(id=it['product'])
                SaleItem.objects.create(sale=sale, product=product, qty=it['qty'], price=it['price'])
                # reduce stock - naive FIFO location  default
                sl = StockLevel.objects.filter(product=product).first()
                if sl:
                    sl.quantity = max(0, sl.quantity - int(it['qty']))
                    sl.save()
        return Response({'id': sale.id, 'invoice_no': sale.invoice_no}, status=status.HTTP_201_CREATED)
