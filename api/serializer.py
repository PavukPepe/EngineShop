from rest_framework import serializers
from adminka.models import Role, Country, Supplier, EngineType, FuelType, Engine, Inventory, EngineReview, News
from django.contrib.auth.models import User, Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class RoleSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'description', 'group']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'code']

class SupplierSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'name', 'country', 'contact_email', 'contact_phone']

class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = ['id', 'name', 'description']

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = ['id', 'name', 'description']

class EngineSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    engine_type = EngineTypeSerializer(read_only=True)
    fuel_type = FuelTypeSerializer(read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Engine
        fields = [
            'id', 'supplier', 'engine_type', 'fuel_type', 'country', 'model',
            'release_year', 'power_hp', 'torque_nm', 'displacement_liters',
            'weight_kg', 'image', 'created_at', 'updated_at'
        ]

class InventorySerializer(serializers.ModelSerializer):
    engine = EngineSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = ['id', 'engine', 'quantity', 'price', 'warehouse_location']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EngineReviewSerializer(serializers.ModelSerializer):
    engine = EngineSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = EngineReview
        fields = ['id', 'engine', 'user', 'rating', 'comment', 'created_at']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']