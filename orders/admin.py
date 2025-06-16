from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'updated_at')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'address')
    list_filter = ('status', 'created_at')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'engine', 'quantity', 'price')
    list_display_links = ('order', 'engine')
    search_fields = ('engine__model', 'order__user__username')
    list_filter = ('quantity',)

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'