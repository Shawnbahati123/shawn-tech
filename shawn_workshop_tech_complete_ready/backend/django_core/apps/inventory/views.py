from rest_framework.viewsets import ModelViewSet
from .models import Supplier, Product, StockLevel
from .serializers import SupplierSerializer, ProductSerializer, StockLevelSerializer

class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StockLevelViewSet(ModelViewSet):
    queryset = StockLevel.objects.all()
    serializer_class = StockLevelSerializer