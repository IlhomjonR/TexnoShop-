from django.urls import path

from orders.views import OrderListView
from .views import create_order

app_name = 'orders'

urlpatterns = [
    path('create-order/<slug:slug>/', create_order, name='create_order'),
    path('orders/', OrderListView.as_view(), name='order_list'),
]
