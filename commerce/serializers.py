from rest_framework.fields import ReadOnlyField
import shortuuid
from django.db.models import fields
from rest_framework import serializers
from .models import  Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):

  

    class Meta:
        model = Order
        #fields = ['price',]
        fields = '__all__'
    
