from rest_framework import serializers
from .models import Order, OrderDetail, ShoppingCar
from app.serializers import CursoSerializer


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'price']  
        #fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderDetail
        fields = ['id', 'order', 'curso', 'quantity', 'price']


class ShoppingCarSerializer(serializers.ModelSerializer):

    #product = CursoSerializer(many=False)
    
    class Meta:
        model = ShoppingCar 
        fields = ['id', 'product', 'price', 'quantity', 'user']


    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class UpGradeSerializer(serializers.Serializer):

    cantidad = serializers.IntegerField()
    class Meta:
        model = ShoppingCar 
        fields = ['id', 'cantidad']

    

class DownGradeSerializer(serializers.Serializer):

    cantidad = serializers.IntegerField()


