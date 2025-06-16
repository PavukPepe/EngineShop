from django import forms
from .models import *

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'description']
        labels = {
            'name': 'Название роли',
            'description': 'Описание',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'code']
        labels = {
            'name': 'Название страны',
            'code': 'Код',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'country', 'contact_email', 'contact_phone']
        labels = {
            'name': 'Название поставщика',
            'country': 'Страна',
            'contact_email': 'Электронная почта',
            'contact_phone': 'Телефон',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (XXX) XXX-XX-XX'}),
        }

class EngineTypeForm(forms.ModelForm):
    class Meta:
        model = EngineType
        fields = ['name', 'description']
        labels = {
            'name': 'Название типа двигателя',
            'description': 'Описание',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class FuelTypeForm(forms.ModelForm):
    class Meta:
        model = FuelType
        fields = ['name', 'description']
        labels = {
            'name': 'Название типа топлива',
            'description': 'Описание',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class EngineForm(forms.ModelForm):
    class Meta:
        model = Engine
        fields = ['supplier', 'engine_type', 'fuel_type', 'country', 'model', 'release_year', 'power_hp', 'torque_nm', 'displacement_liters', 'weight_kg', 'image']
        labels = {
            'supplier': 'Поставщик',
            'engine_type': 'Тип двигателя',
            'fuel_type': 'Тип топлива',
            'country': 'Страна',
            'model': 'Модель',
            'release_year': 'Год выпуска',
            'power_hp': 'Мощность (л.с.)',
            'torque_nm': 'Крутящий момент (Нм)',
            'displacement_liters': 'Объем (литры)',
            'weight_kg': 'Вес (кг)',
            'image': 'Фото двигателя',
        }
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-select'}),
            'engine_type': forms.Select(attrs={'class': 'form-select'}),
            'fuel_type': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'power_hp': forms.NumberInput(attrs={'class': 'form-control'}),
            'torque_nm': forms.NumberInput(attrs={'class': 'form-control'}),
            'displacement_liters': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['engine', 'quantity', 'price', 'warehouse_location']
        labels = {
            'engine': 'Двигатель',
            'quantity': 'Количество',
            'price': 'Цена',
            'warehouse_location': 'Место на складе',
        }
        widgets = {
            'engine': forms.Select(attrs={'class': 'form-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'warehouse_location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EngineReviewForm(forms.ModelForm):
    class Meta:
        model = EngineReview
        fields = ['engine', 'user', 'rating', 'comment']
        labels = {
            'engine': 'Двигатель',
            'user': 'Пользователь',
            'rating': 'Оценка (1-5)',
            'comment': 'Комментарий',
        }
        widgets = {
            'engine': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.Select(attrs={'class': 'form-select'}, choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']
        labels = {
            'title': 'Название',
            'content': 'Содержание',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }