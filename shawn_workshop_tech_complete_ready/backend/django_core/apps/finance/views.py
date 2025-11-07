from rest_framework.viewsets import ModelViewSet
from .models import Expense, FinanceSnapshot
from .serializers import ExpenseSerializer, FinanceSnapshotSerializer

class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class FinanceSnapshotViewSet(ModelViewSet):
    queryset = FinanceSnapshot.objects.all()
    serializer_class = FinanceSnapshotSerializer