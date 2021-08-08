from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import ShoppingCarViewSet, QuantityDowngradeView, QuantityUpgradeView

#router = DefaultRouter()
#router.register('shopping-car', ShoppingCarViewSet.as_view(), name='ShoppingCar')

urlpatterns = [
    path('shopping-car/', ShoppingCarViewSet.as_view(), name='ShoppingCar'),
    path('shopping-car-up/', QuantityUpgradeView.as_view(), name='ShoppingCarUp'),
    path('shopping-car-down/', QuantityDowngradeView.as_view(), name='ShoppingCarDown')
]