from django.urls import path, include
from rest_framework import urlpatterns
from django.urls import path
from .views import Payment
from rest_framework.routers import DefaultRouter
from .views import ShoppingCarViewSet, QuantityDowngradeView, QuantityUpgradeView, OrderView, OrderDetailView

urlpatterns = [
    path('shopping-car/', ShoppingCarViewSet.as_view(), name='ShoppingCar'),
    path('shopping-car-up/', QuantityUpgradeView.as_view(), name='ShoppingCarUp'),
    path('shopping-car-down/', QuantityDowngradeView.as_view(), name='ShoppingCarDown'),
    path('payments/', Payment.as_view(), name='payment'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('order-detail/', OrderDetailView.as_view(), name='order-detail')
]

