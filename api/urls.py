from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoleViewSet, CountryViewSet, SupplierViewSet, EngineTypeViewSet,
    FuelTypeViewSet, EngineViewSet, InventoryViewSet, EngineReviewViewSet, NewsViewSet
)

router = DefaultRouter(trailing_slash=False)
router.register(r'roles', RoleViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'engine-types', EngineTypeViewSet)
router.register(r'fuel-types', FuelTypeViewSet)
router.register(r'engines', EngineViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'engine-reviews', EngineReviewViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]