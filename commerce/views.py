from commerce.serializers import DownGradeSerializer, ShoppingCarSerializer, UpGradeSerializer
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from authentication.models import  User 

from .models import  ShoppingCar, Order as OrderModel, OrderDetail
from app.models import Curso as Product
from .serializers import OrderSerializer, OrderDetailSerializer
from .paypal import Order
from .utils import random_code
from json import loads
from django.http.response import JsonResponse

from rest_framework.response import Response
from rest_framework import serializers, viewsets, generics
from app.models import Curso




class Payment(generics.GenericAPIView):
    serializer_class = OrderSerializer
    #queryset = Curso.objects.all()

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = loads(body_unicode)
        #print(body)
        order_id = body['orderID']
        #print("00000000000000000")
        #print(order_id)

        shopping_cart = ShoppingCar.objects.filter(user=body['user']).all()
        total_price = round(sum(round(d.price * d.quantity, 2) for d in shopping_cart), 2)

        order = Order().get_order(order_id)
        order_price = float(order.result.purchase_units[0].amount.value)

        user = User.objects.get(id=body['user'])
        
        if order_price == total_price:
            return self._order_capture(
                order_id, order_price, request, shopping_cart, user
            )

        return JsonResponse({
            'error': 'Sucedio un error al realizar el cobro'
        })

    def _order_capture(self, order_id, order_price, request, shopping_cart, user):
        order_capture = Order().capture_order(order_id, debug=True)

        code = f'PC-{random_code(5)}'
        
    
        order = OrderModel.objects.create(price=order_price, user=user, code=code)
        if order:
            order_id = order.pk
            for value in shopping_cart:
                OrderDetail.objects.create(order_id=order_id, product_id=value.product.id, quantity=value.quantity, price=value.price)
            ShoppingCar.objects.filter(user=user).delete()

        data = {
            'id': order_capture.result.id,
            'name': order_capture.result.payer.name.given_name
        }
        

        return JsonResponse(data)


class ShoppingCarViewSet(generics.GenericAPIView):

    serializer_class = ShoppingCarSerializer

    def post(self, request, *args, **kwargs):
        body = request.data
        curso_id = body['product']
        product_query = Curso.objects.get(id=curso_id)
        serializer = self.serializer_class(data=request.data)
        user = User.objects.get(id=body['user'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        if product_query:
            price = product_query.precio
            try:
                shopping = ShoppingCar.objects.get(product_id=curso_id, user=user)
                print('curso ya se encuentra en el carrito')
            except ShoppingCar.DoesNotExist:
                shopping = ShoppingCar(product_id=curso_id, price=price, quantity=1, user=user)
                shopping.save()
                print('se agrego el curso al carrito')
        
        return Response(serializer.data)

        
class QuantityUpgradeView(generics.GenericAPIView):

    serializer_class = UpGradeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        shopping_car = ShoppingCar.objects.filter(id=1).first()
        if serializer.is_valid(raise_exception=True):
            cantidad = request.cantidad
            print('serializer')
            print(serializer)
            print('quantity')
            print(shopping_car.quantity)
            if shopping_car:            
                shopping_car.quantity = shopping_car.quantity + cantidad
                shopping_car.save()
        return Response(serializer.data)


class QuantityDowngradeView(generics.GenericAPIView):
    
    serializer_class = DownGradeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        shopping_car = ShoppingCar.objects.get(pk=kwargs['pk'])
        print(shopping_car)
        cantidad = serializer.data
        if shopping_car:
            if shopping_car.quantity > 1:
                shopping_car.quantity = shopping_car.quantity - cantidad
                shopping_car.save()
            elif shopping_car.quantity == 1:
                shopping_car.delete()


class OrderView(generics.GenericAPIView):
   
    serializer_class = OrderSerializer
    def get(self,  request, format=None):
        queryset = OrderModel.objects.all()
        serializer = OrderSerializer( queryset, many=True)
        return Response(serializer.data)


class OrderDetailView(generics.GenericAPIView):
   
    serializer_class = OrderDetailSerializer
    def get(self,  request, format=None):
        queryset = OrderDetail.objects.all()
        serializer = OrderDetailSerializer( queryset, many=True)
        return Response(serializer.data)