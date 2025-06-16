from django.urls import path
from .views import CustomLoginView, logout_view, register, engine_list, add_to_cart, cart_view, update_cart, order_create, order_list, crud_engine
from django.shortcuts import redirect

app_name = 'shop'

urlpatterns = [
    path('', lambda request: redirect('shop:engine_list'), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('engines/', engine_list, name='engine_list'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/update/', update_cart, name='update_cart'),
    path('order/create/', order_create, name='order_create'),
    path('orders/', order_list, name='order_list'),
    path('accounts/profile/', lambda request: redirect('shop:engine_list'), name='profile_redirect'),
    # path('crud/engine/', crud_engine, name='crud_engine'),
]