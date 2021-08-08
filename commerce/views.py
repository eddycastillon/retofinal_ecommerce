from commerce.serialzers import DownGradeSerializer, ShoppingCarSerializer, UpGradeSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, viewsets, generics
from .models import ShoppingCar
from app.models import Curso

# Create your views here.

#@api_view(['POST'])
#def post(self, request, *args, **kwargs):

class ShoppingCarViewSet(generics.GenericAPIView):

    serializer_class = ShoppingCarSerializer

    def post(self, request, *args, **kwargs):
        body = request.POST
        curso_id = body['product_id']
        product_query = Curso.objects.get(id=curso_id)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        if product_query:
            price = product_query.price
            try:
                shopping = ShoppingCar.objects.get(product_id=curso_id, user=request.user)
                print('curso ya se encuentra en el carrito')
            except ShoppingCar.DoesNotExist:
                shopping = ShoppingCar(product_id=curso_id, price=price, quantity=1, user=request.user)
                shopping.save()
                print('se agrego el curso al carrito')
        
        return Response(serializer.data)

        
class QuantityUpgradeView(generics.GenericAPIView):

    serializer_class = UpGradeSerializer
#cantidad = serializer.data
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