from commerce.models import ShoppingCar
from django.contrib import admin

# Register your models here.

@admin.register(ShoppingCar)
class ShoppingCarAdmin(admin.ModelAdmin):

    list_display = ['id', 'product', 'price', 'quantity', 'user']
    search_fields = ['id']