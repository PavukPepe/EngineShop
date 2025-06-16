from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Role, Country, Supplier, EngineType, FuelType, Engine, Inventory, EngineReview, News

# Отменяем стандартную регистрацию модели User
admin.site.unregister(User)


@admin.register(User)
class UsersAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'email')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active',
            'groups'),
        }),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'group')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('name',)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_display_links = ('name',)
    search_fields = ('name', 'code')
    list_filter = ('name',)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'contact_email', 'contact_phone')
    list_display_links = ('name',)
    search_fields = ('name', 'contact_email', 'contact_phone')
    list_filter = ('country',)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


@admin.register(EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('name',)

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Типы двигателей'


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_display_links = ('name',)
    search_fields = ('name', 'description')
    list_filter = ('name',)

    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Типы топлива'


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('model', 'supplier', 'engine_type', 'fuel_type', 'power_hp', 'created_at')
    list_filter = ('supplier', 'engine_type', 'fuel_type', 'country')
    search_fields = ('model', 'supplier__name')
    fields = (
        'supplier', 'engine_type', 'fuel_type', 'country',
        'model', 'release_year', 'power_hp', 'torque_nm',
        'displacement_liters', 'weight_kg', 'image',
    )
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('engine', 'quantity', 'price', 'warehouse_location')
    list_display_links = ('engine',)
    search_fields = ('engine__model', 'warehouse_location')
    list_filter = ('quantity', 'price')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


@admin.register(EngineReview)
class EngineReviewAdmin(admin.ModelAdmin):
    list_display = ('engine', 'user', 'rating', 'created_at')
    list_display_links = ('engine',)
    search_fields = ('engine__model', 'user__username', 'comment')
    list_filter = ('rating', 'created_at')

    class Meta:
        verbose_name = 'Отзыв о двигателе'
        verbose_name_plural = 'Отзывы о двигателях'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'