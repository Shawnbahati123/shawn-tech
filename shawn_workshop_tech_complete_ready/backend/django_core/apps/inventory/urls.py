from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, ProductViewSet, StockLevelViewSet

router = DefaultRouter()
router.register("suppliers", SupplierViewSet)
router.register("products", ProductViewSet)
router.register("stock-levels", StockLevelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]