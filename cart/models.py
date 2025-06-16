from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from adminka.models import Engine

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='cart', verbose_name='Пользователь')
    session_key = models.CharField(max_length=32, null=True, blank=True, verbose_name='Ключ сессии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"Корзина для {self.user.username if self.user else self.session_key}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name='Корзина')
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, verbose_name='Двигатель')
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='Количество')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f"{self.quantity} x {self.engine} в корзине"

    def is_available(self):
        inventory = self.engine.inventory.first()
        return inventory and inventory.quantity >= self.quantity

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'