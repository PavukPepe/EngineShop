from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse, reverse_lazy

from adminka.models import Engine, EngineType, FuelType
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem

def is_admin_or_manager(user):
    return user.groups.filter(name__in=['Администратор', 'Менеджер']).exists()

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('shop:engine_list')

    def form_valid(self, form):
        """Переносим корзину из сессии в модель Cart после авторизации."""
        response = super().form_valid(form)
        self.merge_cart()
        return response

    def merge_cart(self):
        """Слияние корзины из сессии в модель Cart."""
        user = self.request.user
        cart_session = self.request.session.get('cart', {})
        if cart_session:
            cart, created = Cart.objects.get_or_create(user=user)
            for engine_id, quantity in cart_session.items():
                engine = get_object_or_404(Engine, id=engine_id)
                cart_item, created = CartItem.objects.get_or_create(cart=cart, engine=engine)
                cart_item.quantity += quantity
                cart_item.save()
            self.request.session['cart'] = {}

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы.')
    return redirect('shop:home')

@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST.get('email', '')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Имя пользователя уже занято.')
        else:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password)
            )
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Регистрация успешна! Вы вошли в систему.')
                return redirect('shop:engine_list')  # Перенаправление на каталог
            else:
                messages.error(request, 'Ошибка аутентификации после регистрации.')
    return render(request, 'register.html')

def engine_list(request):
    engines = Engine.objects.all()
    query = request.GET.get('q')
    engine_type = request.GET.get('engine_type')
    fuel_type = request.GET.get('fuel_type')

    if query:
        engines = engines.filter(
            Q(model__icontains=query) |
            Q(supplier__name__icontains=query)
        )
    if engine_type:
        engines = engines.filter(engine_type__name=engine_type)
    if fuel_type:
        engines = engines.filter(fuel_type__name=fuel_type)

    paginator = Paginator(engines, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'engine_list.html', {
        'page_obj': page_obj,
        'engine_types': EngineType.objects.all(),
        'fuel_types': FuelType.objects.all(),
        'query': query,
        'selected_engine_type': engine_type,
        'selected_fuel_type': fuel_type
    })

def add_to_cart(request):
    if request.method == 'POST':
        engine_id = request.POST.get('engine_id')
        quantity = int(request.POST.get('quantity', 1))
        engine = get_object_or_404(Engine, id=engine_id)

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, engine=engine)
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart = request.session.get('cart', {})
            cart[str(engine_id)] = cart.get(str(engine_id), 0) + quantity
            request.session['cart'] = cart

        messages.success(request, 'Двигатель добавлен в корзину!')
        return redirect(request.META.get('HTTP_REFERER', reverse('shop:engine_list')))  # Перенаправление на предыдущую страницу

    return redirect('shop:engine_list')  # Резервное перенаправление для GET-запросов

def cart_view(request):
    cart_items = []
    total_price = 0

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        total_price = sum(item.engine.inventory.first().price * item.quantity for item in cart_items if item.engine.inventory.first())
    else:
        cart = request.session.get('cart', {})
        for engine_id, quantity in cart.items():
            engine = get_object_or_404(Engine, id=engine_id)
            inventory = engine.inventory.first()
            if inventory:
                cart_items.append({'engine': engine, 'quantity': quantity, 'inventory': inventory})
                total_price += inventory.price * quantity

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def update_cart(request):
    if request.method == 'POST':
        engine_id = request.POST.get('engine_id')
        quantity = int(request.POST.get('quantity', 1))

        if request.user.is_authenticated:
            cart = get_object_or_404(Cart, user=request.user)
            cart_item = get_object_or_404(CartItem, cart=cart, engine_id=engine_id)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
        else:
            cart = request.session.get('cart', {})
            if quantity > 0:
                cart[str(engine_id)] = quantity
            else:
                cart.pop(str(engine_id), None)
            request.session['cart'] = cart

        messages.success(request, 'Корзина обновлена!')
        return redirect('shop:cart')

    return redirect('shop:cart')

def order_create(request):
    if not request.user.is_authenticated:
        return redirect(f"{reverse('shop:login')}?next={reverse('shop:order_create')}")

    if request.method == 'POST':
        address = request.POST.get('address')
        if not address:
            messages.error(request, 'Укажите адрес доставки')
            return redirect('shop:cart')

        cart = get_object_or_404(Cart, user=request.user)
        cart_items = cart.items.all()

        if not cart_items:
            messages.error(request, 'Корзина пуста')
            return redirect('shop:cart')

        order = Order.objects.create(user=request.user, address=address)
        for item in cart_items:
            inventory = item.engine.inventory.first()
            OrderItem.objects.create(
                order=order,
                engine=item.engine,
                quantity=item.quantity,
                price=inventory.price
            )
            if inventory:
                inventory.quantity -= item.quantity
                inventory.save()

        cart.items.all().delete()
        messages.success(request, 'Заказ успешно оформлен!')
        return redirect('shop:order_list')

    return redirect('shop:cart')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})

@user_passes_test(is_admin_or_manager)
def crud_engine(request):
    return render(request, 'crud_engine.html', {})