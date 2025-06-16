from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from .forms import *

# Shop Views (Public-facing)
@login_required
def engine_list(request):
    engines = Engine.objects.all()
    context = {
        'engines': engines,
        'suppliers': Supplier.objects.all(),
        'engine_types': EngineType.objects.all(),
        'fuel_types': FuelType.objects.all(),
        'countries': Country.objects.all(),
        'current_filters': {
            'supplier': request.GET.get('supplier', ''),
            'engine_type': request.GET.get('engine_type', ''),
            'fuel_type': request.GET.get('fuel_type', ''),
            'country': request.GET.get('country', ''),
            'sort_by': request.GET.get('sort_by', 'model'),
            'order': request.GET.get('order', 'asc'),
        }
    }
    return render(request, 'shop/engine_list.html', context)

@login_required
def cart(request):
    # Placeholder for cart functionality
    return render(request, 'shop/cart.html')

@login_required
def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'shop/order_list.html', {'orders': orders})

@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.save()
            return redirect('shop:order_list')
    else:
        form = OrderForm(initial={'customer': request.user})
    return render(request, 'shop/order_form.html', {'form': form})

# Admin Views (Restricted to superusers)
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

def home(request):
    return render(request, 'base.html')

# Role Views
class RoleListView(AdminRequiredMixin, ListView):
    model = Role
    template_name = 'role/role_list.html'
    context_object_name = 'roles'

class RoleDetailView(AdminRequiredMixin, DetailView):
    model = Role
    template_name = 'role/role_detail.html'
    context_object_name = 'role'

class RoleCreateView(AdminRequiredMixin, CreateView):
    model = Role
    form_class = RoleForm
    template_name = 'role/role_form.html'
    success_url = reverse_lazy('adminka:role_list')

class RoleUpdateView(AdminRequiredMixin, UpdateView):
    model = Role
    form_class = RoleForm
    template_name = 'role/role_form.html'
    success_url = reverse_lazy('adminka:role_list')

class RoleDeleteView(AdminRequiredMixin, DeleteView):
    model = Role
    template_name = 'role/role_confirm_delete.html'
    success_url = reverse_lazy('adminka:role_list')

# Country Views
class CountryListView(AdminRequiredMixin, ListView):
    model = Country
    template_name = 'country/country_list.html'
    context_object_name = 'countries'

class CountryDetailView(AdminRequiredMixin, DetailView):
    model = Country
    template_name = 'country/country_detail.html'
    context_object_name = 'country'

class CountryCreateView(AdminRequiredMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'country/country_form.html'
    success_url = reverse_lazy('adminka:country_list')

class CountryUpdateView(AdminRequiredMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'country/country_form.html'
    success_url = reverse_lazy('adminka:country_list')

class CountryDeleteView(AdminRequiredMixin, DeleteView):
    model = Country
    template_name = 'country/country_confirm_delete.html'
    success_url = reverse_lazy('adminka:country_list')

# Supplier Views
class SupplierListView(AdminRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier/supplier_list.html'
    context_object_name = 'suppliers'

class SupplierDetailView(AdminRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier/supplier_detail.html'
    context_object_name = 'supplier'

class SupplierCreateView(AdminRequiredMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'
    success_url = reverse_lazy('adminka:supplier_list')

class SupplierUpdateView(AdminRequiredMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier/supplier_form.html'
    success_url = reverse_lazy('adminka:supplier_list')

class SupplierDeleteView(AdminRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier/supplier_confirm_delete.html'
    success_url = reverse_lazy('adminka:supplier_list')

# EngineType Views
class EngineTypeListView(AdminRequiredMixin, ListView):
    model = EngineType
    template_name = 'enginetype/enginetype_list.html'
    context_object_name = 'engine_types'

class EngineTypeDetailView(AdminRequiredMixin, DetailView):
    model = EngineType
    template_name = 'enginetype/enginetype_detail.html'
    context_object_name = 'engine_type'

class EngineTypeCreateView(AdminRequiredMixin, CreateView):
    model = EngineType
    form_class = EngineTypeForm
    template_name = 'enginetype/enginetype_form.html'
    success_url = reverse_lazy('adminka:enginetype_list')

class EngineTypeUpdateView(AdminRequiredMixin, UpdateView):
    model = EngineType
    form_class = EngineTypeForm
    template_name = 'enginetype/enginetype_form.html'
    success_url = reverse_lazy('adminka:enginetype_list')

class EngineTypeDeleteView(AdminRequiredMixin, DeleteView):
    model = EngineType
    template_name = 'enginetype/enginetype_confirm_delete.html'
    success_url = reverse_lazy('adminka:enginetype_list')

# FuelType Views
class FuelTypeListView(AdminRequiredMixin, ListView):
    model = FuelType
    template_name = 'fueltype/fueltype_list.html'
    context_object_name = 'fuel_types'

class FuelTypeDetailView(AdminRequiredMixin, DetailView):
    model = FuelType
    template_name = 'fueltype/fueltype_detail.html'
    context_object_name = 'fuel_type'

class FuelTypeCreateView(AdminRequiredMixin, CreateView):
    model = FuelType
    form_class = FuelTypeForm
    template_name = 'fueltype/fueltype_form.html'
    success_url = reverse_lazy('adminka:fueltype_list')

class FuelTypeUpdateView(AdminRequiredMixin, UpdateView):
    model = FuelType
    form_class = FuelTypeForm
    template_name = 'fueltype/fueltype_form.html'
    success_url = reverse_lazy('adminka:fueltype_list')

class FuelTypeDeleteView(AdminRequiredMixin, DeleteView):
    model = FuelType
    template_name = 'fueltype/fueltype_confirm_delete.html'
    success_url = reverse_lazy('adminka:fueltype_list')

# Engine Views
class EngineListView(AdminRequiredMixin, ListView):
    model = Engine
    template_name = 'engine/engine_list.html'
    context_object_name = 'engines'

    def get_queryset(self):
        queryset = super().get_queryset()
        supplier_id = self.request.GET.get('supplier')
        engine_type_id = self.request.GET.get('engine_type')
        fuel_type_id = self.request.GET.get('fuel_type')
        country_id = self.request.GET.get('country')

        if supplier_id:
            queryset = queryset.filter(supplier_id=supplier_id)
        if engine_type_id:
            queryset = queryset.filter(engine_type_id=engine_type_id)
        if fuel_type_id:
            queryset = queryset.filter(fuel_type_id=fuel_type_id)
        if country_id:
            queryset = queryset.filter(country_id=country_id)

        sort_by = self.request.GET.get('sort_by', 'model')
        order = self.request.GET.get('order', 'asc')
        if sort_by in ['model', 'release_year', 'power_hp', 'torque_nm']:
            if order == 'desc':
                sort_by = f'-{sort_by}'
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = Supplier.objects.all()
        context['engine_types'] = EngineType.objects.all()
        context['fuel_types'] = FuelType.objects.all()
        context['countries'] = Country.objects.all()
        context['current_filters'] = {
            'supplier': self.request.GET.get('supplier', ''),
            'engine_type': self.request.GET.get('engine_type', ''),
            'fuel_type': self.request.GET.get('fuel_type', ''),
            'country': self.request.GET.get('country', ''),
            'sort_by': self.request.GET.get('sort_by', 'model'),
            'order': self.request.GET.get('order', 'asc'),
        }
        return context

class EngineDetailView(AdminRequiredMixin, DetailView):
    model = Engine
    template_name = 'engine/engine_detail.html'
    context_object_name = 'engine'

class EngineCreateView(AdminRequiredMixin, CreateView):
    model = Engine
    form_class = EngineForm
    template_name = 'engine/engine_form.html'
    success_url = reverse_lazy('adminka:engine_list')

class EngineUpdateView(AdminRequiredMixin, UpdateView):
    model = Engine
    form_class = EngineForm
    template_name = 'engine/engine_form.html'
    success_url = reverse_lazy('adminka:engine_list')

class EngineDeleteView(AdminRequiredMixin, DeleteView):
    model = Engine
    template_name = 'engine/engine_confirm_delete.html'
    success_url = reverse_lazy('adminka:engine_list')

# Inventory Views
class InventoryListView(AdminRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'inventories'

    def get_queryset(self):
        queryset = super().get_queryset()
        engine_id = self.request.GET.get('engine')

        if engine_id:
            queryset = queryset.filter(engine_id=engine_id)

        sort_by = self.request.GET.get('sort_by', 'quantity')
        order = self.request.GET.get('order', 'asc')
        if sort_by in ['quantity', 'price']:
            if order == 'desc':
                sort_by = f'-{sort_by}'
            queryset = queryset.order_by(sort_by)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['engines'] = Engine.objects.all()
        context['current_filters'] = {
            'engine': self.request.GET.get('engine', ''),
            'sort_by': self.request.GET.get('sort_by', 'quantity'),
            'order': self.request.GET.get('order', 'asc'),
        }
        return context

class InventoryDetailView(AdminRequiredMixin, DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    context_object_name = 'inventory'

class InventoryCreateView(AdminRequiredMixin, CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('adminka:inventory_list')

class InventoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('adminka:inventory_list')

class InventoryDeleteView(AdminRequiredMixin, DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('adminka:inventory_list')

# EngineReview Views
class EngineReviewListView(AdminRequiredMixin, ListView):
    model = EngineReview
    template_name = 'enginereview/enginereview_list.html'
    context_object_name = 'reviews'

class EngineReviewDetailView(AdminRequiredMixin, DetailView):
    model = EngineReview
    template_name = 'enginereview/enginereview_detail.html'
    context_object_name = 'review'

class EngineReviewCreateView(AdminRequiredMixin, CreateView):
    model = EngineReview
    form_class = EngineReviewForm
    template_name = 'enginereview/enginereview_form.html'
    success_url = reverse_lazy('adminka:enginereview_list')

class EngineReviewUpdateView(AdminRequiredMixin, UpdateView):
    model = EngineReview
    form_class = EngineReviewForm
    template_name = 'enginereview/enginereview_form.html'
    success_url = reverse_lazy('adminka:enginereview_list')

class EngineReviewDeleteView(AdminRequiredMixin, DeleteView):
    model = EngineReview
    template_name = 'enginereview/enginereview_confirm_delete.html'
    success_url = reverse_lazy('adminka:enginereview_list')

# News Views
class NewsListView(AdminRequiredMixin, ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_by = self.request.GET.get('sort_by', 'created_at')
        order = self.request.GET.get('order', 'asc')
        if sort_by in ['title', 'created_at']:
            if order == 'desc':
                sort_by = f'-{sort_by}'
            queryset = queryset.order_by(sort_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_filters'] = {
            'sort_by': self.request.GET.get('sort_by', 'created_at'),
            'order': self.request.GET.get('order', 'asc'),
        }
        return context

class NewsDetailView(AdminRequiredMixin, DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

class NewsCreateView(AdminRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('adminka:news_list')

class NewsUpdateView(AdminRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    success_url = reverse_lazy('adminka:news_list')

class NewsDeleteView(AdminRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('adminka:news_list')