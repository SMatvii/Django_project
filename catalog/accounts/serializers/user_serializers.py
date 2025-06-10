from django.contrib.auth.models import User
from rest_framework import serializers

from...products.models import Category, Product, Order, Cart, OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"