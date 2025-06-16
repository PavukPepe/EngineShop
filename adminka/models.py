from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MinValueValidator

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='role', verbose_name='Группа')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Автоматически создаем или обновляем связанную группу
        if not hasattr(self, 'group'):
            self.group = Group.objects.create(name=self.name)
        else:
            self.group.name = self.name
            self.group.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    code = models.CharField(max_length=3, unique=True, verbose_name='Код')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='suppliers', verbose_name='Страна')
    contact_email = models.EmailField(blank=True, verbose_name='Электронная почта')
    contact_phone = models.CharField(max_length=15, blank=True, verbose_name='Телефон')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

class EngineType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Типы двигателей'

class FuelType(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Типы топлива'

class Engine(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='engines', verbose_name='Поставщик')
    engine_type = models.ForeignKey(EngineType, on_delete=models.SET_NULL, null=True, related_name='engines', verbose_name='Тип двигателя')
    fuel_type = models.ForeignKey(FuelType, on_delete=models.SET_NULL, null=True, related_name='engines', verbose_name='Тип топлива')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='engines', verbose_name='Страна')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_year = models.PositiveIntegerField(verbose_name='Год выпуска')
    power_hp = models.PositiveIntegerField(verbose_name='Мощность (л.с.)')
    torque_nm = models.PositiveIntegerField(verbose_name='Крутящий момент (Нм)')
    displacement_liters = models.FloatField(validators=[MinValueValidator(0.1)], null=True, blank=True, verbose_name='Объем (литры)')
    weight_kg = models.PositiveIntegerField(null=True, blank=True, verbose_name='Вес (кг)')
    image = models.ImageField(upload_to='engines/', null=True, blank=True, verbose_name='Фото двигателя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.model} ({self.supplier})"

    class Meta:
        verbose_name = 'Двигатель'
        verbose_name_plural = 'Двигатели'

class Inventory(models.Model):
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, related_name='inventory', verbose_name='Двигатель')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Цена')
    warehouse_location = models.CharField(max_length=100, blank=True, verbose_name='Место на складе')

    def __str__(self):
        return f"{self.engine} - {self.quantity} шт."

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

class EngineReview(models.Model):
    engine = models.ForeignKey(Engine, on_delete=models.CASCADE, related_name='reviews', verbose_name='Двигатель')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviews', verbose_name='Пользователь')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MinValueValidator(5)], verbose_name='Оценка')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Отзыв для {self.engine} от {self.user}"

    class Meta:
        verbose_name = 'Отзыв о двигателе'
        verbose_name_plural = 'Отзывы о двигателях'

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'