from django.urls import path
from .views import *

app_name = 'adminka'

urlpatterns = [
    path('', home, name='home'),

    # Role URLs
    path('roles/', RoleListView.as_view(), name='role_list'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role_detail'),
    path('roles/create/', RoleCreateView.as_view(), name='role_create'),
    path('roles/<int:pk>/update/', RoleUpdateView.as_view(), name='role_update'),
    path('roles/<int:pk>/delete/', RoleDeleteView.as_view(), name='role_delete'),

    # Country URLs
    path('countries/', CountryListView.as_view(), name='country_list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('countries/create/', CountryCreateView.as_view(), name='country_create'),
    path('countries/<int:pk>/update/', CountryUpdateView.as_view(), name='country_update'),
    path('countries/<int:pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),

    # Supplier URLs
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    # EngineType URLs
    path('engine-types/', EngineTypeListView.as_view(), name='enginetype_list'),
    path('engine-types/<int:pk>/', EngineTypeDetailView.as_view(), name='enginetype_detail'),
    path('engine-types/create/', EngineTypeCreateView.as_view(), name='enginetype_create'),
    path('engine-types/<int:pk>/update/', EngineTypeUpdateView.as_view(), name='enginetype_update'),
    path('engine-types/<int:pk>/delete/', EngineTypeDeleteView.as_view(), name='enginetype_delete'),

    # FuelType URLs
    path('fuel-types/', FuelTypeListView.as_view(), name='fueltype_list'),
    path('fuel-types/<int:pk>/', FuelTypeDetailView.as_view(), name='fueltype_detail'),
    path('fuel-types/create/', FuelTypeCreateView.as_view(), name='fueltype_create'),
    path('fuel-types/<int:pk>/update/', FuelTypeUpdateView.as_view(), name='fueltype_update'),
    path('fuel-types/<int:pk>/delete/', FuelTypeDeleteView.as_view(), name='fueltype_delete'),

    # Engine URLs
    path('engines/', EngineListView.as_view(), name='engine_list'),
    path('engines/<int:pk>/', EngineDetailView.as_view(), name='engine_detail'),
    path('engines/create/', EngineCreateView.as_view(), name='engine_create'),
    path('engines/<int:pk>/update/', EngineUpdateView.as_view(), name='engine_update'),
    path('engines/<int:pk>/delete/', EngineDeleteView.as_view(), name='engine_delete'),

    # Inventory URLs
    path('inventories/', InventoryListView.as_view(), name='inventory_list'),
    path('inventories/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventories/create/', InventoryCreateView.as_view(), name='inventory_create'),
    path('inventories/<int:pk>/update/', InventoryUpdateView.as_view(), name='inventory_update'),
    path('inventories/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory_delete'),

    # EngineReview URLs
    path('engine-reviews/', EngineReviewListView.as_view(), name='enginereview_list'),
    path('engine-reviews/<int:pk>/', EngineReviewDetailView.as_view(), name='enginereview_detail'),
    path('engine-reviews/create/', EngineReviewCreateView.as_view(), name='enginereview_create'),
    path('engine-reviews/<int:pk>/update/', EngineReviewUpdateView.as_view(), name='enginereview_update'),
    path('engine-reviews/<int:pk>/delete/', EngineReviewDeleteView.as_view(), name='enginereview_delete'),

    # News URLs
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
]