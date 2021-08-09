from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from authentication.models import  User 

from .models import  ShoppingCart, Order as OrderModel, OrderDetail
from app.models import Curso as Product
from .serializers import OrderSerializer
from .paypal import Order
from .utils import random_code
from json import loads
from django.http.response import JsonResponse




class Payment(generics.GenericAPIView):
    serializer_class = OrderSerializer
    #queryset = Curso.objects.all()

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = loads(body_unicode)
        print(body)
        order_id = body['orderID']
        print("00000000000000000")
        print(order_id)

        shopping_cart = ShoppingCart.objects.filter(user=body['user']).all()
        total_price = round(sum(round(d.price * d.quantity, 2) for d in shopping_cart), 2)

        order = Order().get_order(order_id)
        order_price = float(order.result.purchase_units[0].amount.value)

        #if order_price == total_price:
        if order_price == order_price:
            return self._order_capture(
                order_id, order_price, request, shopping_cart
            )

        return JsonResponse({
            'error': 'Sucedio un error al realizar el cobro'
        })

    def _order_capture(self, order_id, order_price, request, shopping_cart):
        #order_capture = Order().capture_order(order_id, debug=True)

        code = f'PC-{random_code(5)}'
        user = User.objects.get(email='admin@gmail.com')
        print(user)
        order = OrderModel.objects.create(price=order_price, user=user, code=code)
        if order:
            order_id = order.pk
            for value in shopping_cart:
                OrderDetail.objects.create(order_id=order_id, product_id=value.product.id, quantity=value.quantity, price=value.price)
            ShoppingCart.objects.filter(user=user).delete()

        data = {
            'id': order_id,
            #'id': order_capture.result.id,
            'name': order_id
            #'name': order_capture.result.payer.name.given_name
        }
        

        return JsonResponse(data)

# Create your views here.
