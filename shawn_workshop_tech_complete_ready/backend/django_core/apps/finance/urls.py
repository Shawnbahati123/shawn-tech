from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, FinanceSnapshotViewSet

router = DefaultRouter()
router.register("expenses", ExpenseViewSet)
router.register("finance-snapshots", FinanceSnapshotViewSet)

urlpatterns = [
    path("", include(router.urls)),
]