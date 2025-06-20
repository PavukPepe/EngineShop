from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from django.contrib.auth.models import Group
from adminka.models import Role, Country, Supplier, EngineType, FuelType, Engine, Inventory, EngineReview, News
from .serializer import (
    RoleSerializer, CountrySerializer, SupplierSerializer, EngineTypeSerializer,
    FuelTypeSerializer, EngineSerializer, InventorySerializer, EngineReviewSerializer, NewsSerializer
)
from .permissions import (
    CustomRolePermissions, CustomCountryPermissions, CustomSupplierPermissions,
    CustomEngineTypePermissions, CustomFuelTypePermissions, CustomEnginePermissions,
    CustomInventoryPermissions, CustomEngineReviewPermissions, CustomNewsPermissions
)
from rest_framework.pagination import PageNumberPagination
import logging

# Настройка логгера
logger = logging.getLogger(__name__)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RoleViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [CustomRolePermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"RoleViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class CountryViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [CustomCountryPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"CountryViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class SupplierViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomSupplierPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"SupplierViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class EngineTypeViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = EngineType.objects.all()
    serializer_class = EngineTypeSerializer
    permission_classes = [CustomEngineTypePermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"EngineTypeViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class FuelTypeViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    # permission_classes = [CustomFuelTypePermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"FuelTypeViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset

class EngineViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    permission_classes = [CustomEnginePermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"EngineViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(model__icontains=search_query)
        return queryset

class InventoryViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [CustomInventoryPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"InventoryViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(engine__model__icontains=search_query)
        return queryset

class EngineReviewViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = EngineReview.objects.all()
    serializer_class = EngineReviewSerializer
    permission_classes = [CustomEngineReviewPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"EngineReviewViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(comment__icontains=search_query)
        return queryset

class NewsViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [CustomNewsPermissions]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        logger.debug(f"NewsViewSet: User: {self.request.user}, Search query: {search_query}")
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset