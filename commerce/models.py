from django.db import models
from app.models import Curso
from authentication.models import User
# Create your models here.


class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'shopping_carts'
        verbose_name = 'Shopping Cart'
        verbose_name_plural = 'Shopping Carts'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.code

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_details'
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'
