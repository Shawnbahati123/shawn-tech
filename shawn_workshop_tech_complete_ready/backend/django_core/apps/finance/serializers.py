from rest_framework import serializers
from .models import Expense, FinanceSnapshot

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class FinanceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceSnapshot
        fields = '__all__' 