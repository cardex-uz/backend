from rest_framework import serializers

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = "order",
        read_only_fields = "cost",


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        exclude = "customer",
        read_only_fields = "status", "cost"


