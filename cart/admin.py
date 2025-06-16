from django.contrib import admin
from .models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'created_at', 'updated_at')
    list_display_links = ('user', 'session_key')
    search_fields = ('user__username', 'session_key')
    list_filter = ('created_at', 'updated_at')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'engine', 'quantity', 'added_at')
    list_display_links = ('cart', 'engine')
    search_fields = ('engine__model', 'cart__user__username')
    list_filter = ('quantity', 'added_at')

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'